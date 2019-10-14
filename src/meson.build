data = configuration_data()
data.set('message', 'Generated string')
data.set('prefix', get_option('prefix'))

gen_file = configure_file(input: 'gen.cpp.in',
                          output: 'gen.cpp',
                          configuration: data)
gen = library('gen', gen_file, install : true)

src = library('src', 'src.cpp', install : true)

main = executable('main',
                  'main.cpp',
                  link_with : [src, gen],
                  install : true)

pc_install_dir = '@0@/pkgconfig'.format(get_option('libdir'))
foreach pc : ['gen.pc', 'src.pc']
  configure_file(input: pc + '.in',
                 output: pc,
                 configuration : data,
                 install_dir : pc_install_dir)
endforeach
