from ipykernel.kernelapp import IPKernelApp
from .kernel import DotKernel
IPKernelApp.launch_instance(kernel_class=DotKernel)
