import re
import sublime
import sublime_plugin

class KuaijiFindCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		def on_done(index):
			if index >= 0:
				self.view.show_at_center(titleRegions_list[index])


		titles_list=[]
		supTitles_list=[]
		supSeparate='/'
		preRgx='.'
		titleRgx='^'+re.escape(preRgx)+'+[^'+preRgx+'].*(?=:$)'


		titleRegions_list=self.view.find_all(titleRgx)
		for titleRegion in titleRegions_list:
			title=self.view.substr(titleRegion)
			(hierPre,title)=re.match('(^'+re.escape(preRgx)+'+)([^'+preRgx+'].*)', title).groups()
			
			while len(supTitles_list) < len(hierPre):
				if len(supTitles_list) == len(hierPre)-1:
					supTitles_list.append(title)
				else:
					supTitles_list.append('miss')

			supTitles_list[len(hierPre)-1]=title
			del supTitles_list[len(hierPre):]

			titles_list.append([title,supSeparate.join(supTitles_list[0:len(hierPre)-1])])


		sublime.status_message('found '+str(len(titles_list))+' titles')
		self.view.window().show_quick_panel(titles_list, on_done)
