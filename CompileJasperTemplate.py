import sublime
import sublime_plugin
import subprocess

def which(program):
	import os
	def is_exe(fpath):
		return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

	fpath, fname = os.path.split(program)
	if fpath:
		if is_exe(program):
			return program
	else:
		for path in os.environ["PATH"].split(os.pathsep):
			path = path.strip('"')
			exe_file = os.path.join(path, program)
			if is_exe(exe_file):
				return exe_file

	return None

class CompileJasperTemplateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		jasper_executable = which('jasperstarter')
		subprocess.Popen((jasper_executable, 'compile',self.view.file_name()), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )


