####################
## copy subs code
####################
cps_subs_dir='/home/leon/code/PROGRAMS.330/SUBS'

#cp $cps_subs_dir/tgetmod.f .
#cp $cps_subs_dir/mnmarg.f .
#cp $cps_subs_dir/mgtarg.f .
#cp $cps_subs_dir/mchdep.f .
#cp $cps_subs_dir/lgstr.f .


#f2py -h tlegn96.pyf -m tlegn96 tlegn96_subroutine.f mnmarg.f mgtarg.f lgstr.f tio.f mchdep.f  tgetmod.f
f2py --f77flags="-ffixed-line-length-none -O3" --f90flags="-O3" -c tlegn96.pyf tlegn96_subroutine.f mnmarg.f mgtarg.f lgstr.f tio.f mchdep.f tgetmod.f

cp tlegn96.so ..
