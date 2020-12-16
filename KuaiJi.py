import os
import re
import sublime
import sublime_plugin

class FindInFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		def on_done(index):
			if index >= 0:
				self.view.show_at_center(titleRegions_list[index])


		titles_list=[]
		supTitles_list=[]
		supTitles_dict={}
		supTitles=u''
		titleRgx=u'^\.+[^.].*(?=:$)'
		preRgx=u'.'


		titleRegions_list=self.view.find_all(titleRgx)
		for titleRegion in titleRegions_list:
			title=self.view.substr(titleRegion)
			(hierPre,title)=re.match(u'(^\.+)([^.].+)', title).groups()
			supTitles_dict[hierPre]=title
			preIndex=preRgx
			while hierPre != preIndex:
				if preIndex not in supTitles_dict:
					supTitles_dict[preIndex]=u'miss'


				supTitles_list.append(supTitles_dict[preIndex]+u'/')
				preIndex+=preRgx


			titles_list.append([title,supTitles.join(supTitles_list)])
			supTitles_list=[]
			supTitles=u''


		print(titles_list)
		sublime.status_message(u'found'+str(len(titles_list))+u'titles')
		self.view.window().show_quick_panel(titles_list, on_done)
