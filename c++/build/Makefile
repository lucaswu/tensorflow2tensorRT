
# 0=dynamic lib; 1=static lib
LIBTYPE  = 0
TENSORRT = 1

ifeq ($(TENSORRT), 1)           
DEFS = -DTENSORRT
else
DEFS = -DTENSORFLOW
endif


OPENSSL=../../third_party/openssl

TARGETNAME= libksyAI
CUDADIR=/usr/local/cuda
TENSORRTDIR=/usr/local/TensorRT

OUTDIR    = ../../../bin
BINDIR    = ../../bin
OBJDIR    = ../../obj

SRCDIRS    = ../../src
SRCDIRS   += ../../src/gpu
SRCDIRS   += ../../src/gpu/kernel
SRCDIRS   += ../../src/gpu/layers
SRCDIRS   += ../../src/ksy_auth
SRCDIRS   += ../../src/ksy_auth/httpclient
SRCDIRS   += ../../proto/


HDRDIRS0   = ../../interface
HDRDIRS1   = ../../src/ksy_auth
HDRDIRS2   = ../../src/ksy_auth/httpclient
HDRDIRS3   = ../../model
HDRDIRS4   = $(CUDADIR)/include
HDRDIRS5   = ../../model
HDRDIRS6   = ../../src
HDRDIRS10  = $(TENSORRTDIR)/include
HDRDIRS11  = ../../src/gpu
HDRDIRS12  = ../../src/gpu/kernel
HDRDIRS13  = ../../src/gpu/layers
HDRDIRS14  = ../../proto/


ARCHTYPE = -m64

ifeq ($(LIBTYPE), 1)           
TARGETLIB = $(BINDIR)/$(TARGETNAME).a
else
TARGETLIB = $(BINDIR)/$(TARGETNAME).so
endif

CC        = $(shell which g++)
C         = $(shell which gcc)
NVCC 	  = /usr/local/cuda/bin/nvcc
G++       = $(CC) -mpreferred-stack-boundary=4 -fvisibility=hidden
GCC       = $(C) -mpreferred-stack-boundary=4 -fvisibility=hidden

CPPFLAGS  = -O3 -fPIC -std=c++11 $(DEFS)
CFLAGS    = -O3 -fPIC
CUDAFLAG  = -O3 --compiler-options '-fPIC' -std=c++11
LDFLAGS   = -lstdc++ $(ARCHTYPE) -ldl -lpthread -lprotobuf -L $(OPENSSL)/lib -L $(CUDADIR)/lib64 -lcudart -lnppisu -lnppig -L $(TENSORRTDIR)/lib -lnvinfer -lnvinfer_plugin  -Wl,--whole-archive -lcrypto -Wl,--no-whole-archive

CPPFLAGS  += -I$(HDRDIRS0) -I$(HDRDIRS1) -I$(HDRDIRS2) -I$(HDRDIRS3)  -I$(HDRDIRS4) -I$(HDRDIRS3) -I$(HDRDIRS5) -I$(HDRDIRS6) -I$(HDRDIRS7)  -I$(HDRDIRS9) -I$(HDRDIRS10) -I$(HDRDIRS11) -I$(HDRDIRS12) -I$(HDRDIRS13)  -I$(HDRDIRS14)
CFLAGS    += -I$(HDRDIRS0) -I$(HDRDIRS1) -I$(HDRDIRS2) -I$(HDRDIRS3)  -I$(HDRDIRS4) -I$(HDRDIRS3) -I$(HDRDIRS5) -I$(HDRDIRS6) -I$(HDRDIRS7)  -I$(HDRDIRS8)
CUDAFLAG  += -I$(HDRDIRS0) -I$(HDRDIRS1) -I$(HDRDIRS2) -I$(HDRDIRS3) -I$(HDRDIRS4) -I$(HDRDIRS6)  -I$(HDRDIRS7) -I$(HDRDIRS8) -I$(HDRDIRS10) -I$(HDRDIRS11) -I$(HDRDIRS12) -I$(HDRDIRS13) 

SRCEXTS  = .cc .c .cu
HDREXTS  = .h

SMS ?= 60 70
ifeq ($(SMS),)
$(info >>> WARNING - no SM architectures have been specified - waiving sample <<<)
SAMPLE_ENABLED := 0
endif

ifeq ($(GENCODE_FLAGS),)
# Generate SASS code for each SM architecture listed in $(SMS)
$(foreach sm,$(SMS),$(eval GENCODE_FLAGS += -gencode arch=compute_$(sm),code=sm_$(sm)))

# Generate PTX code from the highest SM architecture in $(SMS) to guarantee forward-compatibility
HIGHEST_SM := $(lastword $(sort $(SMS)))
ifneq ($(HIGHEST_SM),)
GENCODE_FLAGS += -gencode arch=compute_$(HIGHEST_SM),code=compute_$(HIGHEST_SM)
endif
endif


SOURCES   = $(foreach d,$(SRCDIRS),$(wildcard $(addprefix $(d)/*,$(SRCEXTS))))
HEADERS   = $(foreach d,$(HDRDIRS),$(wildcard $(addprefix $(d)/*,$(HDREXTS))))
SRC_CPP   = $(filter %.cc,$(SOURCES))
SRC_C     = $(filter %.c,$(SOURCES))
SRC_CUDA  = $(filter %.cu,$(SOURCES))
OBJS      = $(addsuffix .o, $(basename $(SOURCES)))


COMPILE.cc   = $(G++) $(CPPFLAGS) -c
COMPILE.c   = $(GCC) $(CFLAGS) -c
COMPILE.cu   = $(NVCC) $(CUDAFLAG) -c
LINK         = $(G++) $(LDFLAGS)

.PHONY: all objs clean distclean

all: $(TARGETLIB) genCode


ifeq ($(LIBTYPE), 1)
$(TARGETLIB):$(OBJS)
	@if test ! -d $(BINDIR) ; then mkdir $(BINDIR) ; fi
	ar rcs $(TARGETLIB) $(OBJS)
	@echo produce the lib to $(TARGETLIB).
	@if test ! -d $(OUTDIR) ; then mkdir $(OUTDIR) ; fi
	@cp -f $(TARGETLIB) $(OUTDIR)
	@echo copy the lib to $(OUTDIR).

else
$(TARGETLIB):$(OBJS)
	@if test ! -d $(BINDIR) ; then mkdir $(BINDIR) ; fi
	$(LINK) $(OBJS) -shared -Wl,-Bsymbolic -o $@
	@echo produce the lib to $(TARGETLIB).
	@if test ! -d $(OUTDIR) ; then mkdir $(OUTDIR) ; fi
	@cp -f $(TARGETLIB) $(OUTDIR)
	@echo copy the lib to $(OUTDIR).
	@echo $(OPENSSL)
	
endif

genCode:../../src/ksy_auth/genmcode.o  ../../src/genCode/gencode.o
	$(G++) -o ../../src/genCode/genCode $^ -L $(OPENSSL)/lib -lcrypto
	@echo copy the lib to $(OUTDIR).
	@cp -f ../../src/genCode/genCode $(BINDIR)

../../src/genCode/gencode.o: ../../src/genCode/gen_mac_code.cc
	$(G++) -c $< -o $@  -I$(HDRDIRS1) -I$(HDRDIRS6)
		
%.o:%.cc
	$(COMPILE.cc) $< -o $@
%.o:%.c
	$(COMPILE.c) $< -o $@	
%.o:%.cu
	$(COMPILE.cu) $(GENCODE_FLAGS) $< -o $@

clean:
	rm -f $(OBJS) $(TARGETLIB) ../../src/genCode/gencode.o ../../src/genCode/genCode
