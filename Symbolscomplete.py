import sublime, sublime_plugin
import difflib 

class Symbolscomplete(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):
        # return []
        window = sublime.active_window();
        # get results from each tab
        views = window.views();


        #results = [ s[1] for v in window.views() for s in v.symbols() if v.buffer_id() != view.buffer_id() and s[1].lower().startswith(prefix.lower())]
        results = [ s[1] for v in window.views() for s in v.symbols() if get_ratio(prefix,s[1])>0]
        results = [(item,item) for item in results ] #flatten
        results = list(set(results)) # make unique
        results.sort() # sort
        return results



def get_ratio(a,b):
    al = a.lower();
    bl = a.lower();
    return difflib.SequenceMatcher(None,al,al).quick_ratio();