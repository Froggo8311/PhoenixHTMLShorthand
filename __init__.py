# Phoenix HTML Shorthand
def dedent(k):
  if k.startswith('  '):
    return dedent(k[2:])
  else:
    return k

def postbuild(cache):
  pass
  # print(cache)
  
def run(app, config, cache):
  pass
  # global index_page
  # if index_page != None:
    # cache['/']['cont'] = index_page['cont']
  # print(cache)

# global index_page
# index_page = None

def srccompile_file(fdir, urldir, cache, readfile, config):
  psh_in = readfile(fdir, config)['cont']
  psh_in = psh_in.split('\n')
  psh_out = []
  lvl = []
  for line in psh_in:
    line = dedent(line)
    # print(line)
    if dedent(line) == '':
      pass
    elif '*(' and ')*' in line:
      # print('rep *()*')
      line = line.replace('*(', '>').replace(')*', f'</{line.split(" ")[0]}>')
    elif ':{' in line:
      # print('rep :{')
      line = line.replace(':{', '>')
      lvl.append(line.split('\n')[0])
    elif '};' in line:
      # print('rep };')
      end = lvl.pop()
      line = line.replace('};', f'/{end}')
    else:
      line = line + '>'
    
    if not dedent(line) == '':
      line = '<' + line
    print(line)
    psh_out.append(line)
    
  data = {'mime': 'text/html', 'cont': '\n'.join(psh_out)}
    
  url = urldir[4:][:-4]+'.html'
  # if url == '/index.html':
    # url = '/'
    # global index_page
    # index_page = data
    
  cache[url] = data

  if url.endswith('/index.html'):
    cache[url[:-11]] = data

