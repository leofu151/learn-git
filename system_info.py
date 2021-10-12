import platform

def kenerl_info():
	'''
	Return Linux kernel information
	Return Linux kernel information
	'''
	kernel_info = platform.name()
	return {'release': kernel_info.release, 'version': kernel_info.version}

