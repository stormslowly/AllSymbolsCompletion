import sublime, sublime_plugin

class Symbolscomplete(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):
        # return []
        window = sublime.active_window();
        # get results from each tab
        views = window.views();

        results = [ s[1] for v in window.views() for s in v.symbols() if get_ratio(prefix,s[1])>0]
        results = [(item.strip(),format_content(item.strip())) for item in results ] #flatten
        results = list(set(results)) # make unique
        results.sort() # sort
        return results


def get_ratio(a,b):
    al = a.lower();
    bl = b.lower();
    return bl.startswith(a)

def format_content(symbol):
    return symbol.replace("(…)","(${1})") 
