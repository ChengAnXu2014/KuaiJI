import os
import sublime
import sublime_plugin

class FindInFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		def click(index):
			if index >= 0:
				self.view.show_at_center(titleRegions_list[index])


		titles_list=[]
		titleIndex=0
		titleRegex=u''
		if self.view.settings().get(u"kuaiji_title_prefix") and self.view.settings().get(u"kuaiji_title_sufix"):
			titleRegex=u'(?<=^'+self.view.settings().get(u"kuaiji_title_prefix")+u').*(?='+self.view.settings().get(u"kuaiji_title_sufix")+u'$)'
		else:
			titleRegex=u'(?<=^<<).*(?=>>$)'


		titleRegions_list=self.view.find_all(titleRegex)
		self.view.add_regions(u"titles", titleRegions_list, u"head")
		if not titleRegions_list:
			sublime.status_message(u"Can't find any title")
		else:
			for titleRegion in titleRegions_list:
				titleIndex+=1
				if(titleIndex<10):
					prefix=str(titleIndex)+u"         "
				elif(10<=titleIndex<100):
					prefix=str(titleIndex)+u"       "
				else:
					prefix=str(titleIndex)+u"     "


				title=self.view.substr(titleRegion)
				titles_list.append(prefix+title)
			self.view.window().show_quick_panel(titles_list,click)