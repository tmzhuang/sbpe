import cffi
import glob
import platform

# relative to build dir
LIB_BASE = '../libs/'
# compiling libraries statically to get a single binary
EXTRA_SRC = [LIB_BASE + 'subhook/subhook.c']

pltsysname = {'Windows': 'win32', 'Darwin': 'osx', 'Linux': 'elf'}
pltsrc = pltsysname[platform.system()]
pltsrc = LIB_BASE + 'plthook/plthook_{}.c'.format(pltsrc)
EXTRA_SRC.append(pltsrc)  # disabled until it is actually useful

LIBDIRS = []
if platform.system() == 'Windows':
    LIBDIRS.append('../libs/SDL/lib/x86/')

CDEFS = 'generated internals SDL XDL subhook xternPython'.split()


def readfile(name):
    with open(name, 'r') as f:
        content = f.read()
    return content


def build():
    ffibuilder = cffi.FFI()

    for fname in CDEFS:
        ffibuilder.cdef(readfile('cdefs/{}.h'.format(fname)))

    ffibuilder.embedding_api('uint32_t kickstart();')
    ffibuilder.embedding_init_code(readfile('remote.py'))

    ffibuilder.set_source(
        '_remote', readfile('cdefs/remote.c'), sources=EXTRA_SRC,
        libraries=['SDL2'], library_dirs=LIBDIRS,
        define_macros=[('SUBHOOK_STATIC', None)])

    ffibuilder.compile(tmpdir='build', target='remote.bin', verbose=True)


if __name__ == '__main__':
    build()
