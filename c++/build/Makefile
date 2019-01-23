
# 0=dynamic lib; 1=static lib
LIBTYPE  = 0

TARGETNAME= libparser2tensorrt
CUDADIR=/usr/local/cuda
TENSORRTDIR=/usr/local/cuda
PROTOBUF=/usr/local/protobuf

OUTDIR    = ../../bin
BINDIR    = ../bin
OBJDIR    = ../obj
SRCDIRS   = ../src
SRCDIRS   += ../proto
SRCDIRS   += ../test

HDRDIRS0   = ../include
HDRDIRS1   = $(CUDADIR)/include
HDRDIRS2   = $(TENSORRTDIR)/include
HDRDIRS3   = $(PROTOBUF)/include
HDRDIRS4   = ../proto
HDRDIRS5   = ../model



ARCHTYPE = -m64

ifeq ($(LIBTYPE), 1)           
TARGETLIB = $(BINDIR)/$(TARGETNAME).a
else
TARGETLIB = $(BINDIR)/$(TARGETNAME).so
endif

CC        = $(shell which g++)
NVCC 	  = /usr/local/cuda/bin/nvcc
G++       = $(CC) -mpreferred-stack-boundary=4 -fvisibility=hidden

CPPFLAGS  = -O3 -fPIC -std=c++11 
CUDAFLAG  = -O3 --compiler-options '-fPIC' -std=c++11
LDFLAGS   = -lstdc++ $(ARCHTYPE) -ldl -lpthread -L $(PROTOBUF)/lib -lprotobuf -L $(CUDADIR)/lib64 -lcudart  -lnppisu -lnppig -L $(TENSORRTDIR)/lib -lnvinfer -lnvinfer_plugin  #-Wl,--whole-archive 

CPPFLAGS  += -I$(HDRDIRS0) -I$(HDRDIRS1) -I$(HDRDIRS2) -I$(HDRDIRS3)  -I$(HDRDIRS4) -I$(HDRDIRS5)
CUDAFLAG  += -I$(HDRDIRS0) -I$(HDRDIRS1) -I$(HDRDIRS2) -I$(HDRDIRS3)

SRCEXTS  = .cc .cu
HDREXTS  = .h

SMS ?= 50 60 70
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
SRC_CUDA  = $(filter %.cu,$(SOURCES))
OBJS      = $(addsuffix .o, $(basename $(SOURCES)))


COMPILE.cc   = $(G++) $(CPPFLAGS) -c
COMPILE.cu   = $(NVCC) $(CUDAFLAG) -c
LINK         = $(G++) $(LDFLAGS)

.PHONY: all objs clean distclean

all: $(TARGETLIB) test


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
	
endif

test:$(OBJS)
	$(G++) -o $@  $^  $(LDFLAGS)
		 
%.o:%.cc
	$(COMPILE.cc) $< -o $@
%.o:%.cu
	$(COMPILE.cu) $(GENCODE_FLAGS) $< -o $@

clean:
	@echo $(OBJS)
	rm -f $(OBJS) $(TARGETLIB) 
