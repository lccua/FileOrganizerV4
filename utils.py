# third party imports
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QMessageBox


# system imports
import os
import json
import shutil
import hashlib
import pickle

# local imports
import automated_file_organizer_window


file_categories = {
    "Fonts": ['.vfb', '.fnt', '.pfa', '.jfproj', '.vlw', '.pfb', '.woff', '.sfd', '.fot', '.otf', '.woff2', '.ttf', '.bf', '.pmt', '.odttf', '.glif', '.ttc', '.chr', '.fon', '.bdf', '.pfm', '.bmfc', '.fnt', '.amfm', '.mf', '.compositefont', '.etx', '.gxf', '.dfont', '.gdr', '.abf', '.pf2', '.pcf', '.sfp', '.gf', '.mxf', '.tte', '.xfn', '.tfm', '.vnf', '.pfr', '.afm', '.ufo', '.xft', '.eot', '.acfm', '.pk', '.suit', '.ffil', '.nftr', '.txf', '.t65', '.euf', '.mcf', '.cha', '.ytf', '.lwfn', '.f3f', '.fea', '.pft', '.sft'],
    "Audio": ['.fur', '.ftm', '.mtm', '.abc', '.efs', '.weba', '.flp', '.copy', '.mp3', '.ust', '.ec3', '.sf2', '.flac', '.l', '.wproj', '.mui', '.toc', '.asd', '.aup', '.midi', '.mti', '.sngx', '.svp', '.saf', '.xmu', '.als', '.amxd', '.mka', '.cdo', '.minigsf', '.sty', '.akp', '.cwb', '.fev', '.h5s', '.omg', '.igp', '.voxal', '.fsc', '.pna', '.vdj', '.sequence', '.xfs', '.gsf', '.kt3', '.rad', '.xrns', '.vpw', '.acp', '.ptxt', '.itls', '.dsm', '.sds', '.dct', '.slp', '.sc2', '.dff', '.cgrp', '.gp', '.nki', '.mmlp', '.vsq', '.dmse', '.phy', '.sfk', '.m4r', '.mid', '.band', '.gsm', '.gp5', '.rx2', '.4mp', '.apl', '.bun', '.ang', '.pek', '.pcg', '.mscz', '.rmj', '.cue', '.rns', '.uax', '.mmpz', '.dcf', '.abm', '.rex', '.acm', '.g726', '.ogg', '.5xe', '.rip', '.wav', '.sgp', '.logicx', '.gbs', '.alc', '.sfpack', '.afc', '.aria', '.mxl', '.vlc', '.pla', '.ovw', '.acd-zip', '.psm', '.emx', '.cws', '.ncw', '.s3m', '.sfl', '.tg', '.dm', '.vag', '.vyf', '.uni', '.act', '.ac3', '.nrt', '.vqf', '.qcp', '.rol', '.omx', '.frg', '.vsqx', '.bnl', '.q1', '.q2', '.rmx', '.sseq', '.m3u8', '.sesx', '.sdat', '.flm', '.stm', '.rgrp', '.wfp', '.cts', '.sib', '.ptx', '.logic', '.aob', '.wave', '.wma', '.omf', '.wus', '.f32', '.cidb', '.mpu', '.pandora', '.isma', '.pcast', '.trak', '.sbi', '.s3i', '.acd', '.ckb', '.m4a', '.3ga', '.wax', '.mod', '.at3', '.gpk', '.ram', '.vgm', '.w01', '.yookoo', '.med', '.dra', '.oma', '.caf', '.m3u', '.xa', '.wrk', '.uw', '.cwt', '.b4s', '.ftmx', '.h5b', '.pkf', '.note', '.aup3', '.ins', '.m4b', '.aif', '.mtp', '.opus', '.zpa', '.mux', '.svd', '.nkm', '.kmp', '.wpp', '.mus', '.wfm', '.ptt', '.669', '.mus', '.rso', '.bnk', '.gpbank', '.smf', '.cdda', '.swa', '.sxt', '.mptm', '.agm', '.amf', '.mpdp', '.vpl', '.vc3', '.h4b', '.dewf', '.bidule', '.sd', '.mbr', '.ppcx', '.mx3', '.mx4', '.mx5template', '.lof', '.dss', '.a2p', '.dmsa', '.nkx', '.rta', '.iaa', '.aiff', '.caff', '.stap', '.mdr', '.dig', '.wvc', '.bdd', '.pts', '.rti', '.ptm', '.sou', '.wfb', '.cda', '.xspf', '.oga', '.mo3', '.mtf', '.enc', '.cdr', '.tak', '.w64', '.cwp', '.ftm', '.aa', '.ics', '.aac', '.vox', '.bww', '.agr', '.brstm', '.mogg', '.ds', '.dsf', '.sng', '.nml', '.vpr', '.zvd', '.wpk', '.emd', '.bwg', '.cpr', '.lso', '.dtshd', '.aud', '.f4a', '.vmd', '.amr', '.wve', '.mxmf', '.ra', '.dcm', '.iff', '.syh', '.syw', '.rcy', '.wtpt', '.gsflib', '.mmp', '.drg', '.rmi', '.sns', '.u', '.fpa', '.raw', '.nwc', '.vpm', '.nkc', '.shn', '.gpx', '.mpa', '.npl', '.ab', '.mdc', '.dvf', '.igr', '.la', '.lwv', '.ots', '.seq', '.kar', '.tak', '.mx5', '.odm', '.myr', '.uwf', '.ams', '.h5e', '.wv', '.mpga', '.nvf', '.obw', '.xsp', '.ds2', '.song', '.psf', '.adt', '.xm', '.m4p', '.mmm', '.musx', '.avastsounds', '.a2m', '.5xb', '.all', '.dts', '.vip', '.peak', '.cfa', '.dls', '.fzf', '.vgz', '.pac', '.wwu', '.bwf', '.rcd', '.mt2', '.ksc', '.fdp', '.aaxc', '.musicxml', '.rsn', '.zpl', '.rng', '.streamdeckaudio', '.g721', '.nra', '.slx', '.efq', '.efk', '.rdvxz', '.fms', '.au', '.krz', '.sma', '.hbe', '.k26', '.scs11', '.nsa', '.sng', '.ssp', '.nsmpproj', '.msmpl_bank', '.nsmp', '.wut', '.psf1', '.dw', '.nksf', '.rpl', '.gig', '.conform', '.m3up', '.ssm', '.dpdoc', '.sfz', '.capobundle', '.vb', '.ceol', '.koz', '.gbproj', '.hsb', '.pca', '.fzv', '.sppack', '.vap', '.groove', '.psf2', '.acd-bak', '.hca', '.m5p', '.koz', '.nmsv', '.sap', '.syn', '.8svx', '.rfl', '.amz', '.ksf', '.ape', '.jam', '.a2b', '.dmc', '.pho', '.sd', '.ptf', '.adv', '.mpc', '.clp', '.usf', '.pno', '.aifc', '.smp', '.csh', '.miniusf', '.ove', '.adg', '.aax', '.dmf', '.vrf', '.snd', '.ses', '.tta', '.xmf', '.mp2', '.mts', '.kfn', '.r1m', '.prg', '.nks', '.rbs', '.ovw', '.rts', '.smpx', '.ult', '.5xs', '.rvx', '.psy', '.snd', '.vtx', '.mmf', '.voc', '.stx', '.nkb', '.mpd', '.mgv', '.a2i', '.s3z', '.vmo', '.ppc', '.smp', '.pvc', '.bap', '.usflib', '.exs', '.bank', '.sfap0', '.ntn', '.f64', '.g723', '.adts', '.td0', '.expressionmap', '.sd2f', '.rbs', '.emp', '.wfd', '.ams', '.snd', '.txw', '.sfs', '.ptcop', '.jspf', '.fft', '.repeaks', '.narrative', '.cpt', '.ay', '.minipsf', '.dsf', '.a2w', '.svx', '.mte', '.sd2', '.minipsf2', '.ariax', '.wtpl', '.rax', '.ofr', '.pbf', '.jbx', '.cel', '.msv', '.vmf', '.a2t', '.vmf'],
    "Video": ['.str', '.ttml', '.objection', '.swf', '.aep', '.mkv', '.pz', '.plot', '.sfd', '.piv', '.psv', '.prproj', '.kine', '.dream', '.xyt', '.kdenlive', '.pic', '.anm', '.plotdoc', '.veg', '.msdvd', '.wlmp', '.inp', '.drp', '.aec', '.dcr', '.bik', '.mswmm', '.pac', '.amc', '.webm', '.mse', '.wpl', '.dir', '.cine', '.scm', '.vpj', '.fcp', '.fbr', '.evo', '.dcr', '.sub', '.rmvb', '.mp4', '.srt', '.vob', '.flc', '.clpi', '.sbt', '.tsv', '.mxf', '.ifo', '.vp6', '.m4s', '.dmsm', '.cpvc', '.3gp', '.vsp', '.vtt', '.camproj', '.meta', '.av1', '.mvd', '.hdmov', '.ivr', '.dmx', '.wmmp', '.smv', '.m4u', '.tbc', '.rec', '.mpeg', '.aepx', '.trp', '.swi', '.rcd', '.mp4v', '.video', '.sqz', '.mani', '.d3v', '.amx', '.ser', '.mgv', '.screenflow', '.rms', '.vc1', '.mepx', '.kmproject', '.flv', '.psh', '.asf', '.dmsm3d', '.jtv', '.pmf', '.arcut', '.mpsub', '.siv', '.zm2', '.ale', '.tvshow', '.rcut', '.g2m', '.dpa', '.mys', '.gfp', '.ncor', '.dv4', '.wmv', '.dxr', '.mproj', '.mp4.infovid', '.mpv', '.xmv', '.dat', '.zmv', '.m1v', '.ts', '.trec', '.3gp2', '.idx', '.scc', '.dv', '.264', '.rxr', '.mvp', '.m2t', '.iva', '.mj2', '.rm', '.m4v', '.cme', '.dzm', '.bup', '.camrec', '.dash', '.mjpg', '.tix', '.theater', '.dnc', '.exi', '.mnv', '.bk2', '.ogv', '.vro', '.stx', '.awlive', '.wp3', '.ismv', '.f4p', '.m2ts', '.vgz', '.wvm', '.dzp', '.dvr', '.tp', '.dream', '.mpg', '.mov', '.dmb', '.int', '.ffd', '.ktn', '.dzt', '.qtch', '.ircp', '.cst', '.f4f', '.mmp', '.avv', '.ppj', '.sedprj', '.camv', '.bdt2', '.bik2', '.fbr', '.pclx', '.vii', '.mep', '.mv', '.tivo', '.dvr-ms', '.izz', '.avb', '.sfvidcap', '.rdb', '.zoom', '.bsf', '.gts', '.fli', '.zm3', '.izzy', '.264', '.3mm', '.jdr', '.bnp', '.pds', '.mts', '.wvx', '.playlist', '.cpi', '.sbk', '.vep', '.3g2', '.h264', '.dav', '.mvp', '.sfera', '.dvdmedia', '.xesc', '.vid', '.60d', '.mp2v', '.movie', '.xvid', '.g64', '.ddat', '.san', '.d2v', '.890', '.yuv', '.lvix', '.aaf', '.ism', '.f4v', '.mpl', '.hevc', '.ogx', '.media', '.mp21', '.hdv', '.mk3d', '.vproj', '.xlmv', '.moi', '.mvex', '.dck', '.g64x', '.rsx', '.tsp', '.qtl', '.pro', '.jss', '.m4f', '.divx', '.r3d', '.vcr', '.bdmv', '.ogm', '.lrv', '.3gpp', '.m2p', '.rv', '.wcp', '.avchd', '.mpg4', '.nuv', '.swt', '.spl', '.wm', '.k3g', '.ced', '.bu', '.tvlayer', '.3gpp2', '.tdt', '.braw', '.meps', '.ntp', '.dpg', '.rum', '.pdrproj', '.avi', '.xml', '.wrf', '.movie', '.exo', '.mpe', '.lrec', '.3p2', '.arf', '.flic', '.ave', '.bdt3', '.vp7', '.bmc', '.m2a', '.nfv', '.lsx', '.tvs', '.moov', '.tpd', '.w32', '.jmv', '.rmp', '.dmsd', '.aet', '.aetx', '.prel', '.vcpf', '.wxp', '.mjp', '.mp5', '.f4m', '.mvc', '.edl', '.asx', '.imovieproj', '.vr', '.nvc', '.wmd', '.y4m', '.bvr', '.irf', '.bdm', '.ajp', '.ftc', '.prtl', '.otrkey', '.smil', '.vse', '.pgi', '.epv', '.wtv', '.avd', '.mve', '.tvrecording', '.dif', '.axv', '.avp', '.m2v', '.imovielibrary', '.avs', '.mpl', '.vdr', '.plproj', '.tod', '.sbz', '.hkm', '.mtv', '.m21', '.imoviemobile', '.ismc', '.evo', '.flh', '.sub', '.zm1', '.tda3mt', '.tpr', '.rvl', '.alpx', '.fpdx', '.vbc', '.smk', '.sdv', '.m21', '.dvx', '.peg', '.rvid', '.ttxt', '.lfpackage', '.pxv', '.ivf', '.roq', '.cmmtpl', '.rcrec', '.vfz', '.cmproj', '.qt', '.bmk', '.vcv', '.amv', '.mpgindex', '.tp0', '.projector', '.dvt', '.n3r', '.aegraphic', '.sec', '.gxf', '.photoshow', '.wmx', '.insv', '.dad', '.par', '.qtm', '.rmd', '.pns', '.yog', '.pvr', '.gcs', '.wot', '.crec', '.xel', '.clk', '.nsv', '.vix', '.thp', '.av', '.xfl', '.smi', '.ravi', '.dv-avi', '.fcproject', '.pssd', '.dce', '.ssa', '.gifv', '.vs4', '.bs4', '.lvf', '.qsv', '.byu', '.blz', '.tmv', '.seq', '.fcarch', '.proqc', '.vlab', '.vfw', '.m1pg', '.mod', '.ffm', '.mpls', '.kux', '.modd', '.mxv', '.vf', '.viewlet', '.qtz', '.vdo', '.aecap', '.vem', '.dlx', '.el8', '.pro4dvd', '.axm', '.cmrec', '.spryzip', '.jts', '.imovieproject', '.wsve', '.flx', '.cmmp', '.axp', '.xej', '.ezt', '.usf', '.exp', '.smi', '.moff', '.h265', '.cmv', '.dmss', '.fbz', '.cip', '.stl', '.pva', '.eyetv', '.avs', '.mqv', '.wgi', '.avr', '.rcproject', '.svi', '.eye', '.avc', '.camtemplate', '.h266', '.anydesk', '.skm', '.cx3', '.rts', '.qtindex', '.cam', '.vmlt', '.vmlf', '.mgjson', '.dmsd3d', '.drc', '.vsr', '.anx', '.vp5', '.wfsp', '.pro5dvd', '.cdxl', '.avs', '.mvy', '.gvp', '.mp21', '.mepj', '.av3', '.rp', '.tid', '.sml', '.jnr', '.vsh', '.pmp', '.h263', '.vft'],
    "Images": ['.hipnc', '.bbmodel', '.crz', '.mesh', '.md5anim', '.ddp', '.part', '.real', '.gh', '.c4d', '.duf', '.fsh', '.blend', '.mcsg', '.smd', '.dff', '.makerbot', '.m3d', '.iv', '.phy', '.thing', '.usd', '.dsv', '.mc5', '.zt', '.vpd', '.atm', '.cfg', '.pmx', '.mdl', '.x', '.fx', '.xaf', '.mix', '.lxf', '.nm', '.x3d', '.mu', '.mtz', '.an8', '.psa', '.mdx', '.3ds', '.p3d', '.vox', '.cg', '.flt', '.m3d', '.cso', '.3d2', '.mesh', '.3mf', '.obp', '.wft', '.ma', '.pl0', '.br7', '.cbddlp', '.trace', '.stel', '.dae', '.tme', '.hdz', '.mhm', '.ive', '.3dxml', '.p3l', '.md5camera', '.n3d', '.md5mesh', '.p4d', '.tilt', '.gmf', '.t3d', '.ghx', '.pp2', '.amf', '.cmdb', '.llm', '.ccp', '.3d4', '.irr', '.facefx', '.atl', '.prm', '.v3d', '.bip', '.animset', '.e57', '.ppz', '.grs', '.sh3d', '.skp', '.reality', '.z3d', '.anm', '.anim', '.ds', '.psk', '.obj', '.t3d', '.xmf', '.rcs', '.lnd', '.3da', '.pz2', '.pkg', '.gltf', '.sdb', '.igi', '.crf', '.ifc', '.lxo', '.dwf', '.pkg', '.p5d', '.mnm', '.fcp', '.mb', '.meb', '.prc', '.dn', '.mxm', '.ccb', '.mgf', '.blk', '.des', '.tri', '.a8s', '.chr', '.anim', '.mqo', '.sis', '.mxs', '.off', '.cg3', '.p3m', '.mrml', '.xsi', '.fbx', '.3dm', '.sc4model', '.3dp', '.m3g', '.a3d', '.a2c', '.nif', '.hip', '.mdd', '.b3d', '.pmd', '.spv', '.bif', '.album', '.v3v', '.fcz', '.hrz', '.ms3d', '.obz', '.vsh', '.x3g', '.fpf', '.tcn', '.usdz', '.dsa', '.bld', '.mcz', '.msh', '.arexport', '.fg', '.ol', '.fxt', '.3dl', '.bro', '.ply', '.sh3f', '.3dmf', '.cgfx', '.u3d', '.w3d', '.chr', '.shp', '.geo', '.arm', '.kfm', '.xr', '.br4', '.nxs', '.fxl', '.gmt', '.wrp', '.bvh', '.lws', '.arfx', '.cm2', '.mud', '.hlsl', '.ums', '.par', '.pro', '.vroid', '.fxs', '.ktz', '.grn', '.mc', '.cmf', '.mtl', '.c3d', '.mtx', '.max', '.s', '.pmd', '.vvd', '.lwo', '.d3d', '.act', '.msh', '.srf', '.vs', '.glf', '.ydl', '.iges', '.glsl', '.cpy', '.vmd', '.egg', '.sbsar', '.f3d', '.veg', '.qc', '.glb', '.br6', '.sgn', '.aof', '.dsb', '.csd', '.session', '.vue', '.bio', '.cmod', '.csm', '.cal', '.wrl', '.igs', '.3df', '.maxc', '.pgal', '.pl2', '.brg', '.cr2', '.gmmod', '.tvm', '.3dc', '.pzz', '.fxm', '.visual_processed', '.c3z', '.p3r', '.fig', '.dsf', '.vob', '.nff', '.prv', '.vp', '.pz3', '.mesh', '.ik', '.daz', '.kmcobj', '.xmm', '.dif', '.dfs', '.clara', '.kmc', '.smc', '.fnc', '.s3g', '.fxa', '.3dc', '.jcd', '.dse', '.visual', '.dbm', '.p21', '.skl', '.tmd', '.cmz', '.mdg', '.xof', '.previz', '.3dmk', '.spline', '.shapr', '.iavatar', '.vrm', '.j3o', '.arpatch', '.hxn', '.arprojpkg', '.fpj', '.3dw', '.dmc', '.thl', '.atf', '.irrmesh', '.pro', '.vrl', '.sm', '.fry', '.mc6', '.drf', '.hr2', '.v3o', '.fp', '.p2z', '.primitives_processed', '.ltz', '.vtx', '.xpr', '.cas', '.aoi', '.m3', '.prefab', '.pl1', '.br5', '.fun', '.ddd', '.sbfres', '.ogf', '.dbs', '.br3', '.fp3', '.xrf', '.cms', '.mat', '.dbc', '.n2', '.lp', '.jas', '.wow', '.mmpp', '.glm', '.ts1', '.oct', '.3dx', '.rft', '.tps', '.bsk', '.tri', '.fc2', '.pigs', '.rad', '.ldm', '.dsi', '.si', '.mpj', '.exp', '.fsq', '.glslesf', '.egm', '.rad', '.3d', '.lps', '.r3d', '.pat', '.sto', '.yaodl', '.vso', '.dbl', '.xv0', '.dso', '.asat', '.primitives', '.mp', '.nsbta', '.3dv', '.dsi', '.cal', '.stc', '.vac', '.igm', '.xaf', '.cga', '.chrparams', '.xsf', '.hd2', '.fpe', '.csf', '.mcx-8', '.zvf', '.emcam', '.svf', '.tgo', '.igmesh', '.tmo', '.pigm', '.caf', '.3don', '.lt2', '.mot', '.animset_ingame', '.facefx_ingame', '.vmo', '.arproj', '.brk', '.fbm', '.dsd', '.bto', '.tddd', '.fuse', '.rds', '.wrz', '.anim', '.rig', '.ray', '.cr2', '.raf', '.rw2', '.erf', '.nrw', '.nef', '.arw', '.rwz', '.eip', '.dng', '.bay', '.dcr', '.gpr', '.raw', '.crw', '.3fr', '.sr2', '.k25', '.kc2', '.mef', '.dng', '.cs1', '.orf', '.mos', '.kdc', '.cr3', '.ari', '.srf', '.srw', '.j6i', '.fff', '.mrw', '.x3f', '.mfw', '.rwl', '.pef', '.iiq', '.cxi', '.nksc', '.mdc', '.bif', '.jxl', '.sprite2', '.icon', '.afphoto', '.xpm', '.psdc', '.sumo', '.lrpreview', '.pxd', '.ase', '.mnr', '.psd', '.gif', '.ptex', '.snagx', '.sprite3', '.avatar', '.bpg', '.png', '.ysp', '.sprite', '.tga', '.flif', '.hdr', '.tpf', '.dds', '.clip', '.sai', '.spr', '.piskel', '.ct', '.jpeg', '.ipick', '.8ci', '.skitch', '.pcx', '.wic', '.vicar', '.qoi', '.nwm', '.psp', '.kra', '.oc4', '.linea', '.oplc', '.accountpicture-ms', '.tbn', '.ff', '.sld', '.dib', '.plp', '.aps', '.ppp', '.pdn', '.jpg', '.webp', '.heif', '.jps', '.pm', '.ota', '.lip', '.tfc', '.itc2', '.pwp', '.pov', '.xcf', '.exr', '.fits', '.wbz', '.lzp', '.mng', '.wbc', '.ktx', '.msp', '.psdx', '.73i', '.djvu', '.cpc', '.ppf', '.usertile-ms', '.cdc', '.ozj', '.tiff', '.bmp', '.2bp', '.ecw', '.jls', '.snag', '.ipv', '.tm2', '.jpc', '.mpf', '.px', '.spp', '.pi2', '.pdd', '.pmg', '.pat', '.pfi', '.rgf', '.pbm', '.jpf', '.rpf', '.nol', '.heic', '.urt', '.nlm', '.8pbs', '.pni', '.vna', '.pixela', '.cmr', '.kfx', '.drz', '.pnc', '.icn', '.pspimage', '.cdg', '.stex', '.mdp', '.tg4', '.tn', '.dgt', '.vrimg', '.jng', '.fil', '.dtw', '.fpx', '.aseprite', '.fbm', '.fac', '.vpe', '.mdp', '.jpe', '.iwi', '.bmq', '.awd', '.ptg', '.apng', '.jxr', '.psp', '.tif', '.pgm', '.i3d', '.ppm', '.psb', '.thm', '.cpt', '.ozt', '.pns', '.1sc', '.zif', '.cpd', '.j2k', '.ljp', '.viff', '.pic', '.jbig2', '.wb0', '.avifs', '.pp5', '.vrphoto', '.can', '.otb', '.can', '.art', '.wbm', '.mpo', '.g3n', '.wb2', '.wbmp', '.cals', '.ktx2', '.gmbck', '.pam', '.bmz', '.spa', '.lmnr', '.sph', '.001', '.xbm', '.sig', '.arr', '.info', '.mcs', '.procreate', '.pgf', '.abm', '.hdp', '.pic', '.sid', '.pjpg', '.sig', '.bti', '.cimg', '.lbm', '.ce', '.face', '.pictclipping', '.pe4', '.pxd', '.gim', '.int', '.tex', '.jpg2', '.djv', '.ufo', '.pzs', '.qtif', '.lif', '.agp', '.pvr', '.pnt', '.jbf', '.ilbm', '.vda', '.kdi', '.rcl', '.riff', '.oci', '.jp2', '.oc3', '.oti', '.tif', '.vss', '.hf', '.rtl', '.jpx', '.sup', '.gro', '.rsr', '.hif', '.ais', '.awd', '.wb1', '.prw', '.jia', '.cit', '.sfc', '.gp4', '.apd', '.rli', '.s2mv', '.jpg_large', '.dcm', '.insp', '.qmg', '.v', '.thumb', '.mbm', '.lb', '.pcd', '.wdp', '.hpi', '.pxm', '.wi', '.neo', '.jif', '.ithmb', '.ras', '.ncd', '.bmc', '.snagproj', '.wmp', '.bmx', '.rif', '.ica', '.pse', '.sai2', '.spe', '.kodak', '.cin', '.msk', '.zif', '.pxz', '.sdr', '.targa', '.avif', '.max', '.t2b', '.ivue', '.srf', '.pop', '.kic', '.pc2', '.texture', '.gpd', '.sff', '.wpb', '.pp4', '.gmspr', '.dic', '.pc1', '.pjp', '.mbm', '.svslide', '.tjp', '.mix', '.myl', '.pixadex', '.oc5', '.picnc', '.drp', '.hdrp', '.jbig', '.dmi', '.pza', '.ab3', '.psxprj', '.ozb', '.avb', '.rgb', '.wbp', '.fsthumb', '.j2c', '.monosnippet', '.sktz', '.cid', '.fppx', '.monopic', '.fpos', '.skm', '.gih', '.bm2', '.gbr', '.pzp', '.sky', '.kra~', '.cd5', '.qti', '.ipx', '.360', '.gcdp', '.dm4', '.spj', '.dpx', '.afx', '.agif', '.art', '.pxr', '.dcx', '.psf', '.pano', '.zvi', '.sun', '.9.png', '.8ca', '.ora', '.jfi', '.dt2', '.cut', '.pspbrush', '.j', '.bw', '.sgd', '.apx', '.sva', '.dicom', '.ncr', '.pyxel', '.xwd', '.ddt', '.bss', '.sim', '.u', '.mac', '.pac', '.cpg', '.gfie', '.jpd', '.rcu', '.rle', '.shg', '.odi', '.pap', '.ggr', '.jtf', '.ndpi', '.cal', '.jb2', '.skypeemoticonset', '.qif', '.jiff', '.cam', '.sfw', '.ink', '.jfif', '.svs', '.tps', '.rgba', '.oe6', '.sob', '.epp', '.aic', '.sbp', '.miff', '.mxi', '.pjpeg', '.tub', '.acorn', '.jbr', '.scn', '.uga', '.jwl', '.mrb', '.ugoira', '.sct', '.ivr', '.mat', '.yuv', '.ddb', '.rsb', '.hr', '.mipmaps', '.pov', '.gfb', '.pi1', '.sep', '.ptx', '.ptk', '.8xi', '.smp', '.wvl', '.mic', '.rvg', '.sgi', '.rri', '.omf', '.pnm', '.jbg', '.adc', '.y', '.csf', '.mrxs', '.c4', '.dc6', '.ldoc', '.vmu', '.psdb', '.palm', '.dc2', '.bs', '.jas', '.fax', '.nct', '.pspframe', '.six', '.mip', '.cpx', '.fsymbols-art', '.gvrs', '.oir', '.npsd', '.wbd', '.ric', '.vic', '.pfr', '.pc3', '.icpr', '.pbs', '.psptube', '.xface', '.pe4', '.t2k', '.acr', '.upf', '.colz', '.pal', '.dm3', '.thm', '.sid', '.brn', '.vdoc', '.pxicon', '.qptiff', '.g3f', '.trif', '.frm', '.dvl', '.scn', '.vst', '.tsr', '.kpg', '.cps', '.cpbitmap', '.pix', '.ptx', '.brt', '.tla', '.wpe', '.pts', '.scn', '.bmf', '.rgb', '.blkrt', '.ic3', '.ic2', '.ic1', '.iphotoproject', '.svg', '.svgz', '.vstm', '.ai', '.vsdx', '.afdesign', '.cdr', '.gvdesign', '.ep', '.cmx', '.apm', '.slddrt', '.epsf', '.fh8', '.fcm', '.vstx', '.dpr', '.eps', '.csy', '.fh10', '.wmf', '.pfd', '.fh9', '.cdmz', '.cdd', '.drw', '.ps', '.lmk', '.pobj', '.cdrapp', '.ft9', '.glox', '.fh4', '.psid', '.smf', '.vsd', '.odg', '.std', '.drw', '.fxg', '.fh7', '.igx', '.dpp', '.pmg', '.drawio', '.ink', '.xar', '.emz', '.ecs5', '.ssk', '.nodes', '.plt', '.vst', '.drawit', '.tex.emz', '.aic', '.fhd', '.xmmat', '.cvd', '.scv', '.vsdm', '.cvx', '.ac6', '.otg', '.pd', '.svm', '.pen', '.fig', '.ait', '.plt', '.puppet', '.cddz', '.egc', '.wpg', '.rdl', '.sk', '.ft8', '.hpgl', '.cdx', '.pixil', '.mvg', '.hpg', '.pict', '.dia', '.cdtx', '.vectornator', '.hvif', '.pat', '.gsd', '.sketch', '.fh11', '.ydr', '.vml', '.mgc', '.asy', '.clarify', '.imd', '.mp', '.tpl', '.jsl', '.idea', '.esc', '.cvs', '.wmz', '.emf', '.mmat', '.fh5', '.sk1', '.maker', '.fh3', '.epgz', '.mgtx', '.cdtz', '.tne', '.cvi', '.gstencil', '.mgcb', '.sk2', '.cvg', '.tlc', '.ink', '.snagstyles', '.shapes', '.wpi', '.ezdraw', '.ylc', '.cvxcad', '.scut5', '.drawing', '.sxd', '.dhs', '.ovr', '.graffle', '.dxb', '.ded', '.sda', '.vec', '.stn', '.abc', '.svf', '.cv5', '.ink', '.cgm', '.ftn', '.fmv', '.fh6', '.cil', '.ac5', '.af3', '.fif', '.cnv', '.cdx', '.cdsx', '.sketchpad', '.pl', '.af2', '.dcs', '.ft10', '.zgm', '.pic', '.awg', '.design', '.mgmx', '.hpl', '.ddrw', '.ufr', '.ovp', '.pct', '.fs', '.hgl', '.xmmap', '.ft7', '.artb', '.pfv', '.gks', '.cdmm', '.art', '.cor', '.dpx', '.dsf', '.gem', '.yal', '.ccx', '.cag', '.xpr', '.mgmt', '.ds4', '.ft11', '.cvdtpl', '.cdmt', '.ndtx', '.ndx', '.ndb', '.cdmtz', '.amdn', '.dsg', '.qcc', '.cdt', '.mgmf', '.gtemplate', '.pcs', '.vbr', '.cwt', '.gls', '.mgs', '.pws', '.igt', '.nap', '.p'],
    "Documents": ['.chai', '.drmz', '.flo', '.fsd', '.xmt', '.chait', '.pdfxml', '.afpub', '.xtp', '.lsc', '.ap', '.mfp', '.cst', '.elp', '.fd2', '.sbv', '.pdf', '.inx', '.pdo', '.hcr', '.ifd', '.lbl', '.cedprj', '.ltf', '.mwl', '.ola', '.cal', '.mcsp', '.anh', '.mif', '.psproj', '.pgs', '.isd', '.pdr', '.icap', '.fey', '.hpt', '.gsp', '.fp3', '.cdf', '.lst', '.ppx', '.studio3', '.cl2arc', '.mml', '.zdp', '.inp', '.fm', '.fcdt', '.hmk', '.smmx', '.pub', '.csd', '.blk', '.bcf', '.btw', '.pcl', '.4ui', '.pmd', '.fr3', '.flb', '.mfo', '.dtx', '.zno', '.vfc', '.pzf', '.idms', '.infopathxml', '.clkd', '.wlp', '.gde', '.xps', '.rels', '.idml', '.pnh', '.dtp', '.pmx', '.pff', '.afp', '.dot', '.comicdoc', '.prn', '.form', '.qxd', '.pfl', '.p65', '.fax', '.jtp', '.oxps', '.av', '.clt', '.webtemplate', '.mrg', '.cl2tpl', '.cwt', '.indl', '.idap', '.incx', '.de', '.ind', '.ildoc', '.q3c', '.rmr', '.cph', '.cld', '.incd', '.pex', '.drmx', '.fdd', '.rsm', '.indd', '.bmml', '.zdl', '.psr', '.hfd', '.template', '.mdi', '.opd', '.qxp', '.gwb', '.compositiontemplate', '.t2d', '.lld', '.xif', '.xzfx', '.rwt', '.pdm', '.pm5', '.spl', '.cl2doc', '.comiclife', '.folio', '.sp', '.pwt', '.fxm', '.dra', '.rlf', '.jtx', '.imx', '.avery', '.fadein', '.env', '.max', '.spl7', '.rap', '.lpdf', '.ofd', '.psg', '.article', '.rpc', '.pder', '.eddx', '.book', '.book', '.pm6', '.publication', '.dpd', '.snp', '.tds', '.xsn', '.pdf-1', '.bk', '.caj', '.ptx', '.enc', '.ppp', '.lbl', '.indt', '.gofin', '.sdt', '.cd2', '.mars', '.bro', '.ch3', '.imm', '.pdg', '.sublime-snippet', '.afbook', '.aftemplate', '.cdoc', '.el4', '.frt', '.nsa', '.flowchart', '.rb4', '.omp', '.mvdx', '.clkc', '.inds', '.ebrf', '.cdml', '.mailstationery', '.cbf', '.consis', '.qpt', '.vp', '.fgc', '.imtx', '.isaletemplate', '.icml', '.edrwx', '.pxl', '.cpe', '.dwdoc', '.sjd', '.rpx', '.adf', '.zds', '.icmt', '.bcp', '.wmga', '.mga', '.nud', '.xdw', '.cov', '.wwf', '.pzfx', '.qdf', '.dcx', '.uxf', '.pdh', '.tp3', '.dtl', '.qxb', '.frf', '.npp', '.wpt', '.rfd', '.mft', '.webtheme', '.mvtx', '.isale', '.cw', '.cl2lyt', '.hft', '.gdocx', '.indb', '.biz', '.qxt', '.clkb', '.vpd', '.sbk', '.fpe', '.spub', '.bro', '.csz', '.frdoc', '.pdwr', '.pm4', '.pa', '.simp', '.cndx', '.oo3template', '.dmtemplate', '.mtc', '.mvd', '.studio', '.comic', '.hpd', '.ao', '.scut4', '.gem', '.hwdt', '.crtr', '.lab', '.bpf', '.zfx', '.pds', '.pwb', '.bmpr', '.kitsp', '.jsd', '.ispx', '.cadoc', '.clkbd', '.minder', '.booktemplate', '.indp', '.lma', '.rptr', '.inct', '.inlx', '.fp', '.cpy', '.rwt', '.sma', '.flw', '.jwc', '.wcp', '.cvw', '.idpk', '.frm', '.pdw', '.pdp', '.adb', '.totalslayout', '.pjl', '.mcsx', '.pde', '.fdt', '.antmpl', '.pdz', '.jtx', '.isallic', '.mbbk', '.adf'],
    "Executables": ['.fap', '.apk', '.jar', '.ahk', '.cmd', '.ipa', '.run', '.xbe', '.0xe', '.workflow', '.u3p', '.bms', '.8ck', '.bin', '.exe', '.bat', '.vlx', '.sk', '.air', '.elf', '.x86_64', '.xap', '.gadget', '.app', '.shortcut', '.widget', '.x86', '.appimage', '.rbf', '.fba', '.pif', '.mpk', '.mcr', '.ac', '.com', '.xlm', '.sh', '.tpk', '.73k', '.script', '.scpt', '.command', '.out', '.rxe', '.scb', '.ba_', '.ps1', '.paf.exe', '.scar', '.scr', '.isu', '.xex', '.coffee', '.ex_', '.fas', '.tcp', '.action', '.ebs2', '.celx', '.acc', '.rfu', '.ex5', '.hta', '.89k', '.nexe', '.xbap', '.ecf', '.cgi', '.fxp', '.vpm', '.plsc', '.ws', '.rpj', '.azw2', '.dld', '.mlx', '.cof', '.js', '.caction', '.wsh', '.vbs', '.icd', '.vxp', '.mcr', '.ex_', '.iim', '.phar', '.cheat', '.ex4', '.a7r', '.shb', '.fpi', '.esh', '.server', '.wcm', '.dek', '.gpe', '.pex', '.exe1', '.jsf', '.jsx', '.acr', '.pyc', '.pwc', '.ear', '.mel', '.vexe', '.zl9', '.plx', '.mm', '.snap', '.pyo', '.mcr', '.epk', '.ms', '.exe', '.uvm', '.hms', '.gm9', '.vbscript', '.rgs', '.otm', '.actc', '.atmx', '.applescript', '.frs', '.paf', '.n', '.prg', '.widget', '.mrc', '.csh', '.wiz', '.spr', '.cyw', '.sct', '.ebs', '.gs', '.e_e', '.ebm', '.mrp', '.osx', '.xqt', '.fky', '.app', '.ygh', '.fas', '.prg', '.kx', '.actm', '.udf', '.mxe', '.rox', '.seed', '.kix', '.cel', '.app', '.tms', '.tiapp', '.ezs', '.thm', '.beam', '.vbe', '.jse', '.prg', '.wpk', '.hpf', '.dmc', '.rfs', '.exz', '.s2a', '.msl', '.scptd', '.mhm', '.ls', '.xys', '.sca', '.prc', '.wpm', '.ms', '.ipk', '.ita', '.wsf', '.eham', '.qit', '.es', '.arscript', '.lo', '.rbx', '.mem', '.sapk', '.ebacmd', '.mam', '.ncl', '.ksh', '.upx', '.dxl', '.ham', '.btm', '.gpu', '.mio', '.pvd', '.vdo', '.ipf', '.ds', '.exopc', '.mac', '.sbs', '.cfs', '.asb', '.sts', '.mamc', '.p', '.afmacros', '.afmacro', '.rpg', '.89z', '.pxo', '.uw8', '.srec', '.mlappinstall', '.qpx', '.ore', '.ezt', '.73p', '.smm', '.bns'],
    "System": ['.admx', '.rmt', '.reg', '.shsh2', '.aml', '.vga', '.cur', '.itemdata-ms', '.ani', '.clb', '.regtrans-ms', '.nt', '.service', '.wdgt', '.icns', '.dll', '.deskthemepack', '.inf_loc', '.iconpackage', '.searchconnector-ms', '.hve', '.pk2', '.dvd', '.dmp', '.desklink', '.lnk', '.vx_', '.hiv', '.theme', '.qvm', '.mdmp', '.lockfile', '.ebd', '.htt', '.ftf', '.sys', '.elf', '.library-ms', '.pck', '.sfcache', '.asec', '.ico', '.firm', '.ion', '.rc1', '.manifest', '.prop', '.nfo', '.000', '.mui', '.etl', '.bin', '.edj', '.cgz', '.mod', '.bash_history', '.zone.identifier', '.timer', '.msc', '.pwl', '.ci', '.menu', '.mapimail', '.h1s', '.prefpane', '.dat', '.cm0013', '.adm', '.scr', '.efi', '.cab', '.fx', '.log1', '.wdf', '.bashrc', '.mlc', '.lfs', '.sdb', '.fota', '.msstyles', '.mobileconfig', '.pit', '.c32', '.sys', '.73u', '.trx_dll', '.pnf', '.mtz', '.sbn', '.webpnp', '.hhk', '.pdr', '.0', '.dthumb', '.208', '.bcd', '.drv', '.bash_profile', '.dit', '.mbr', '.ins', '.img3', '.pro', '.ioplist', '.plasmoid', '.3fs', '.mui_cccd5ae0', '.diagcab', '.hdmp', '.cat', '.drpm', '.pol', '.aos', '.sdt', '.shd', '.nb0', '.ppd', '.cpl', '.pat', '.msp', '.savedsearch', '.chs', '.bio', '.cannedsearch', '.vxd', '.1', '.mbn', '.cm0012', '.sbf', '.nls', '.job', '.ax', '.8cu', '.wpx', '.crash', '.kext', '.hlp', '.fpbf', '.cnt', '.2fs', '.idx', '.8xu', '.prf', '.configprofile', '.ps2', '.log2', '.sqm', '.adml', '.panic', '.chg', '.schemas', '.ime', '.dfu', '.cpq', '.tdz', '.shsh', '.wlu', '.lex', '.4', '.swp', '.emerald', '.ntfs', '.b84', '.0', '.journal', '.ffx', '.utv', '.grp', '.386', '.odex', '.lst', '.wer', '.database_uuid', '.dev', '.blf', '.saver', '.hcd', '.evt', '.hhc', '.adv', '.ko', '.dimax', '.group', '.chk', '.provisionprofile', '.str', '.kdz', '.metadata_never_index', '.2', '.ipod', '.icl', '.tha', '.nlt', '.printerexport', '.im4p', '.trashinfo', '.dic', '.devicemetadata-ms', '.profile', '.flg', '.pid', '.cht', '.bmk', '.networkconnect', '.pfx', '.mum', '.ruf', '.mi4', '.atahd', '.nbh', '.cpi', '.ffo', '.bom', '.cap', '.prt', '.kbd', '.evtx', '.mydocs', '.ks', '.spl', '.xrm-ms', '.customdestinations-ms', '.bk2', '.cpr', '.lm', '.rcv', '.mem', '.sprx', '.scf', '.efires', '.ftr', '.mun', '.hsh', '.bk1', '.dlx', '.sefw', '.self', '.thumbnails', '.trash', '.hpj', '.diagpkg', '.sin', '.escopy', '.tbres', '.mmv', '.img2', '.ifw', '.uce', '.wgz', '.kc', '.xfb', '.gmmp', '.cmo', '.rfw', '.trashes', '.so.0', '.scap', '.grl', '.ozip', '.ps1', '.dss', '.dock', '.me', '.automaticdestinations-ms', '.lpd', '.fl1', '.3', '.ffa', '.msstyle', '.kwi', '.rs', '.key', '.ppm', '.fts', '.ius', '.rc2', '.vdex', '.idi', '.jetkey', '.sb', '.vgd', '.bud', '.5', '.push_deviceid', '.lpd', '.iptheme', '.diagcfg', '.wph', '.7', '.6', '.rco', '.qky', '.dyc', '.8', '.jpn', '.localized', '.kl', '.fid', '.ta', '.internetconnect', '.spx', '.cdmp', '.ftg', '.ffl', '.89u', '.its', '.dub', '.tco2', '.roku', '.kor', '.bbfw', '.xgf', '.mrm', '.mrc', '.tno', '.b83', '.ann', '.reglnk', '.help', '.diffbase', '.rvp', '.im4m', '.dat', '.doc', '.sty', '.smf', '.dotx', '.adoc', '.lst', '.man', '.upd', '.gform', '.fpt', '.sam', '.dotm', '.gsite', '.embed', '.ltx', '.qbl', '.dsc', '.wtt', '.diz', '.save', '.fcf', '.me', '.docx', '.hs', '.mnt', '.ltxd', '.lxfml', '.story', '.b', '.eio', '.lue', '.fountain', '.mpd', '.tmdx', '.gpd', '.readme', '.apt', '.odm', '.ans', '.vnt', '.org', '.fbl', '.aww', '.log', '.gdoc', '.ipf', '.dtex', '.klg', '.fadein.template', '.cec', '.pwdpl', '.tex', '.rpt', '.txt', '.nfo', '.rft', '.lis', '.gsd', '.aim', '.docm', '.tlb', '.dropbox', '.asc', '.rst', '.lst', '.dxb', '.opeico', '.scm', '.fodt', '.ipynb', '.wps', '.u3i', '.tmvx', '.asc', '.text', '.wpt', '.emulecollection', '.wpd', '.bf', '.jarvis', '.bib', '.1st', '._docx', '.md5.txt', '.rtf', '.bib', '.wps', '.ott', '.wpw', '.gscript', '.etf', '.knt', '.tfrproj', '.rad', '.luf', '.jnp', '.xy', '.aty', '.tm', '.dm', '.bdr', '.gtable', '.ris', '.pages', '.textclipping', '.cod', '.strings', '.err', '.docz', '.copf', '.wri', '.fdx', '.run', '.klg', '.faq', '.msg', '.scc', '.odt', '.fdt', '.se', '.gjam', '.eml', '.kes', '.omfl', '.rtx', '.tmd', '.gmap', '.mbox', '.lnk42', '.saf', '.lp2', '.etx', '.bean', '.dfti', '.license', '.pwd', '.sgm', '.charset', '.bdp', '.fdr', '.appodeal', '.note', '.dca', '.qdl', '.dx', '.ipspot', '.stw', '.gslides', '.bibtex', '.bad', '.jis', '.xwp', '.dvi', '.shim', '.cast', '.sdm', '.odif', '.ngloss', '.rvf', '.sxw', '.odo', '.rtfd', '.602', '.ndoc', '.utf8', '.wpt', '.vwr', '.emlx', '.sla', '.xwp', '.vcf', '.psw', '.tab', '.sdoc', '.p7s', '.sublime-project', '.eit', '.trelby', '.hwp', '.chord', '.docxml', '.abw', '.idx', '.uot', '.xyw', '.sms', '.frt', '.hwp', '.plain', '.pwi', '.xy3', '.jp1', '.wpd', '.hbk', '.zzs', '.prt', '.latex', '.now', '.pvm', '.bml', '.pwr', '.tpc', '.ytdl', '.graph', '.pages-tef', '.mml', '.dat', '.arc', '.bloonset', '.fluid', '.jlqm', '.md', '.highland', '.calca', '.scriv', '.sfx', '.sla.gz', '.mwd', '.bna', '.notes', '.rzn', '.hht', '.mwp', '.mellel', '.boc', '.lbt', '.njk', '.scrivx', '.wp', '.tnl', '.wp7', '.wp4', '._doc', '.zrtf', '.pimx', '.safetext', '.xdl', '.mw', '.flr', '.fdf', '.btd', '.cnm', '.sam', '.xbdoc', '.utxt', '.joe', '.err', '.act', '.ort', '.mell', '.lwp', '.pfx', '.wpl', '.wpd', '.lyx', '.odp', '.euc', '.hz', '.crwl', '.wbk', '.ascii', '.ofl', '.jtd', '.session', '.dgs', '.plantuml', '.wp6', '.tdf', '.unauth', '.btxt', '.fft', '.prt', '.fwdn', '.rtd', '.awt', '.gpn', '.sp1', '.mss', '.tvj', '.xbplate', '.pmo', '.awp', '.quid', '.ltr', '.gv', '.dwd', '.openbsd', '.sxg', '.sdw', '.njx', '.vct', '.xyp', '.pu', '.rzk', '.nb', '.wtx', '.xwp', '.sct', '.nwctxt', '.del', '.lyt', '.description', '.ocr', '.tmv', '.wpa', '.tdf', '.bbs', '.ase', '.dne', '.ebp', '.dxp', '.cws', '.xdl', '.sgt', '.wg', '.fgs', '.uof', '.zzq', '.brx', '.bwd', '.sublime-workspace', '.mailsignature', '.tid', '.webdoc', '.vpdoc', '.sw3', '.fdxt', '.pwdp', '.unx', '.ptnx', '.vw', '.meltem', '.skcard', '.lnt', '.iil', '.bxt', '.qpf', '.pvj', '.nwm', '.loop', '.cyi', '.nwp', '.kwd', '.wsd', '.emf', '.wp5', '.zw', '.jrtf', '.gthr', '.min', '.pdpcmd', '.wn', '.scw', '.fds', '.gmd', '.mcw', '.dox','.xlsx', '.xls', '.xlsm', '.def', '.123', '.xlr', '.xl', '.dex', '.pmvx', '.numbers-tef', '.xlsb', '.ots', '.nb', '.sxc', '.gnumeric', '.xltm', '.ods', '.cell', '.presto', '.chip', '.xar', '.fods', '.mar', '.bks', '.numbers', '.rdf', '.edxz', '.cts', '.wq2', '.tmv', '.efu', '._xlsx', '.imp', '.pmd', '.nmbtemplate', '.sdc', '.xltx', '._xls', '.fp', '.pmdx', '.gsheet', '.ogwu', '.xlshtml', '.ncss', '.ast', '.qpw', '.dis', '.wks', '.12m', '.gnm', '.wq1', '.xlsmhtml', '.ess', '.ogw', '.edx', '.aws', '.wkq', '.wks', '.xlthtml', '.fcs', '.pmv', '.hcdt', '.stc', '.uos', '.wr1', '.tmvt', '.dfg', '.wku', '.wki', '.wls'],
    "Settings": ['.gxt', '.godot', '.stb', '.style', '.mycolors', '.officeui', '.eqp', '.copreset', '.skz', '.vstpreset', '.vital', '.flw', '.set', '.aux', '.alx', '.dsd', '.pmp', '.sif', '.cnf', '.iss', '.themepack', '.hd3d', '.settings', '.nsx', '.irs', '.vqc', '.oss', '.cfg', '.sbv', '.cfg', '.bs7', '.tsi', '.pkg', '.rproj', '.sed', '.rmskin', '.xui', '.lh3d', '.wcz', '.fvp', '.cfg', '.fxp', '.prm', '.xtp', '.prfpset', '.lrtemplate', '.skin', '.udcx', '.a2theme', '.cex', '.tscproj', '.isp', '.mmrc', '.tpf', '.vssettings', '.ovpn', '.nri', '.dinfo', '.rdp', '.mst', '.cui', '.vim', '.asl', '.aco', '.blob', '.cuix', '.mds', '.cfg', '.s2ml', '.l4d', '.btsearch', '.aip', '.3dl', '.rll', '.icm', '.the', '.dolphinview', '.msn', '.atz', '.asef', '.bcp', '.ihw', '.motr', '.propdesc', '.mnu', '.vcpref', '.trx', '.iip', '.qss', '.lva', '.m2s', '.icst', '.npv4', '.chx', '.pr', '.uis', '.c2r', '.wme', '.osdx', '.zon', '.atc', '.fetchmirror', '.adpp', '.cnf', '.skin', '.tdesktop-theme', '.qtp', '.boot', '.aiu', '.qvpp', '.tlo', '.obt', '.lrsmcol', '.ptb', '.qrc', '.qbtheme', '.wal', '.costyle', '.tsk', '.dcst', '.dcl', '.kpl', '.dbg', '.dok', '.vitalbank', '.properties', '.rps', '.gid', '.mst', '.xtreme', '.conf', '.xpaddercontroller', '.obi', '.bin', '.conf', '.ehi', '.application', '.look', '.pc3', '.sfo', '.mcl', '.pip', '.clg', '.atn', '.rcf', '.ffx', '.xdr', '.sol', '.inf', '.cmp', '.onetoc2', '.profile', '.downloadhost', '.icd', '.iss', '.ds_store', '.zap', '.settingcontent-ms', '.psc1', '.ctb', '.xms', '.acv', '.ftp', '.ini', '.odc', '.wfc', '.acrobatsecuritysettings', '.ksf', '.cpx', '.tmtheme', '.gps', '.nkp', '.moef', '.dicproof', '.uct', '.ft', '.dsx', '.directory', '.appref-ms', '.scpresets', '.plist', '.wfp', '.fd', '.vbox', '.rdf', '.bgi', '.cva', '.psf', '.idpp', '.vmxf', '.ipcc', '.rdw', '.avs', '.wms', '.duck', '.lfo', '.tpark', '.nvp', '.np4', '.opt', '.vmc', '.ps1xml', '.ins', '.chl', '.prf', '.emm', '.ops', '.nps', '.pjs', '.blw', '.eqf', '.ptf', '.msm', '.bcmx', '.eftx', '.vnc', '.fcc', '.act', '.wmz', '.bks', '.acb', '.ens', '.kbd', '.mof', '.a2m', '.wve', '.spp', '.gmw', '.vps', '.gpl', '.alv', '.wcx', '.wsz', '.qxw', '.dxp', '.cskin', '.icursorfx', '.enz', '.epp', '.props', '.moti', '.ruleset', '.pref', '.mlk', '.sz', '.vue', '.zpi', '.dr5', '.tsz', '.vph', '.csplan', '.mxs', '.oem', '.exportedui', '.hwt', '.gtp', '.fat', '.csf', '.kys', '.smt', '.tdf', '.vlt', '.pal', '.cpg', '.slt', '.rts', '.fmt', '.ngrr', '.policy', '.ica', '.synw-proj', '.bau', '.sw2', '.vsprops', '.ssl2', '.prx', '.lvf', '.pie', '.pmj', '.startupinfo', '.utz', '.rpk', '.gws', '.flst', '.dar', '.otz', '.prf', '.sqd', '.pmc', '.xst', '.acw', '.ste', '.ars', '.grd', '.ewprj', '.ini', '.asp', '.ase', '.key', '.fc', '.icc', '.reg', '.hid', '.mpt', '.all', '.xpl', '.p2m', '.camp', '.cdt', '.pgp', '.net', '.mns', '.mtf', '.motn', '.mcw', '.vmcx', '.jkm', '.ddf', '.vimrc', '.ht', '.storyisttheme', '.sss', '.jdf', '.dcp', '.xlb', '.dsw', '.comp', '.axt', '.pdp', '.sl', '.thmx', '.theme', '.scribe', '.jws', '.upf', '.fmp', '.pio', '.lcc', '.ahl', '.oms', '.trk', '.ga', '.nvc', '.cmate', '.exe4j', '.json.crypt14', '.t3d', '.slbk', '.phb', '.ath', '.hme', '.material', '.cursor', '.dvtcolortheme', '.srs', '.frames', '.mailhost', '.ski', '.ix', '.mskn', '.wc', '.cptm', '.spf', '.pctl', '.nji', '.rdo', '.chromaeffects', '.xsosd', '.nwv', '.wf4', '.overlay', '.bitpim', '.snagtheme', '.tsm', '.ppkg', '.sxie', '.flmpst', '.growlticket', '.otpu', '.eql', '.mgk', '.eum', '.rwstyle', '.kcb', '.tvtemplate', '.box', '.vtpr', '.wsb', '.ncfg', '.npfx', '.cos', '.stt', '.vcomps', '.ndc', '.rad', '.fbt', '.pxb', '.ahu', '.wif', '.onc', '.ikmp', '.ini', '.ave', '.mmp', '.ftpquota', '.arg', '.qat', '.nd', '.prf', '.userprofile', '.tvc', '.itt', '.gin', '.terminal', '.typeit4me', '.tts', '.xur', '.dtsconfig', '.ahs', '.zpf', '.work', '.drm', '.ask', '.sch', '.iaf', '.asw', '.ctbodyfitting', '.mxskin', '.joy', '.twc', '.sgt', '.spj', '.vbx6settings', '.std', '.ams', '.skn', '.kds', '.awcav', '.fwt', '.aom', '.brg', '.rfq', '.cdrt', '.xtodvd', '.ast', '.pro5template', '.iit', '.gtkrc', '.rct', '.cpf', '.acb', '.dsf', '.cpr', '.vmx', '.fth', '.snx', '.lop', '.vmpl', '.psp', '.mask', '.mmdc', '.gqsx', '.gcsx', '.sh3l', '.xcu', '.qf', '.zon', '.deft', '.lightkeyproj', '.pdadj', '.bcp', '.dun', '.ssl', '.abs', '.psy', '.xvm', '.dxls', '.gvimrc', '.csaplan', '.pxg', '.mpdconf', '.mobirise', '.spfx', '.cyberduckprofile', '.cyberducklicense', '.lxsopt', '.wzconfig', '.qvt', '.ikf', '.lyt', '.blt', '.profimail', '.gps', '.exp', '.cps', '.pml', '.raskinplace', '.clr', '.fnc', '.msw'],
    "Data": ['.h13', '.txd', '.mdl', '.vmt', '.xem', '.nbp', '.bld', '.flt', '.hyv', '.nitf', '.pptx', '.loc', '.nrl', '.rsv', '.adx', '.met', '.dat', '.ppsm', '.cel', '.tdb', '.ppt', '.bin', '.flo', '.wjr', '.ebuild', '.h17', '.tax2010', '.prs', '.trk', '.wtb', '.azz', '.topc', '.kdc', '.aifb', '.vok', '.xft', '.mmc', '.plw', '.capt', '.quickendata', '.ta9', '.sq', '.t20', '.bgt', '.qb2017', '.dif', '.ald', '.poi', '.t05', '.prdx', '.dm2', '.fsc', '.drl', '.rgo', '.ral', '.sqr', '.abcd', '.kpr', '.tt20', '.mosaic', '.ncorx', '.not', '.hdf', '.ldif', '.obb', '.adt', '.ggb', '.cub', '.tmx', '.mdf', '.prj', '.menc', '.fcpevent', '.jef', '.tbl', '.opx', '.otln', '.mls', '.pcb', '.cdx', '.blg', '.contact', '.edi', '.bdic', '.pc', '.vcs', '.ali', '.pps', '.rox', '.clp', '.zmc', '.aam', '.t12', '.exx', '.rfa', '.lms', '.jph', '.vdf', '.pka', '.ova', '.ip', '.qrp', '.mai', '.enl', '.grf', '.net', '.egp', '.roadtrip', '.vsx', '.ttk', '.quicken2015', '.ndx', '.oo3', '.kpf', '.zap', '.tax2022', '.dockzip', '.uwl', '.livereg', '.grade', '.tax2009', '.ink', '.photoslibrary', '.odp', '.opju', '.sds', '.xlf', '.wdf', '.dcmd', '.wab', '.tcc', '.ckt', '.jnt', '.cav', '.fcs', '.a6p', '.rp', '.ovf', '.xlt', '.acc', '.tar', '.lib', '.q09', '.fdb', '.pab', '.phb', '.qpb', '.dvo', '.pcr', '.u10', '.mwf', '.t10', '.pdx', '.q08', '.potm', '.mdl', '.iif', '.imt', '.rvt', '.rdb', '.emlxpart', '.keychain', '.rbt', '.rsc', '.pfc', '.uccapilog', '.3dr', '.lcm', '.fdb', '.rfo', '.bvp', '.dsz', '.h12', '.hst', '.l6t', '.pj2', '.mbg', '.ppf', '.crtx', '.key', '.in', '.obj', '.bcm', '.idx', '.mmp', '.clg', '.gedcom', '.ppsx', '.qvw', '.vdb', '.xml', '.ptf', '.sdf', '.fox', '.acs', '.slx', '.sav', '.pdb', '.notebook', '.bgl', '.usr', '.box', '.pkt', '.xfd', '.ii', '.dsy', '.ev', '.ret', '.pdx', '.dvdproj', '.bci', '.t18', '.qdf', '.aby', '.lmx', '.rcg', '.svf', '.cma', '.pro6plx', '.mnc', '.dfproj', '.aw', '.pks', '.mox', '.i5z', '.grv', '.fob', '.trd', '.sen', '.mno', '.hda', '.slp', '.oeaccount', '.mpkt', '.xpt', '.gwk', '.sc45', '.rpt', '.tsv', '.mpp', '.moho', '.exif', '.voi', '.pptm', '.tra', '.flp', '.otp', '.ofc', '.pkb', '.emb', '.one', '.gs', '.sps', '.anme', '.paf', '.lvm', '.iba', '.pds', '.ffwp', '.seo', '.mjk', '.xlc', '.efx', '.celtx', '.lbl', '.inx', '.stm', '.pst', '.mmap', '.ofx', '.vcf', '.aae', '.myi', '.quicken2017', '.enex', '.qb2013', '.grk', '.gdt', '.fmat', '.hl', '.rte', '.ptz', '.t07', '.tdl', '.qb2011', '.pdas', '.asnd', '.trs', '.wgt', '.t13', '.tax2018', '.jrprint', '.pxl', '.wpc', '.csv', '.npl', '.xrdml', '.cap', '.gbr', '.xsl', '.pxj', '.t19', '.gpi', '.xmcd', '.pmo', '.omp', '.dpn', '.lp7', '.slk', '.xpg', '.4dv', '.idx', '.ged', '.kpz', '.vxml', '.tax2015', '.windowslivecontact', '.fpsl', '.mdsx', '.tdt', '.tb', '.rpp', '.vce', '.potx', '.stykz', '.lsf', '.tpf', '.m', '.gcw', '.vcd', '.tax2017', '.prj', '.sim', '.dam', '.mdj', '.tef', '.ima', '.qb2014', '.twb', '.ptn', '.dcm', '.out', '.rte', '.adcp', '.tax2013', '.abp', '.cdx', '.cdf', '.ptb', '.tbk', '.sdp', '.tdm', '.xpj', '.itx', '.qmtf', '.cvn', '.mcdx', '.pcapng', '.xslt', '.ulf', '.mex', '.pd4', '.t06', '.jdb', '.xrp', '.t16', '.ppf', '.dsb', '.id2', '.hs2', '.rnq', '.cna', '.mmp', '.fop', '.wgt', '.dii', '.xmlper', '.xfo', '.sar', '.te3', '.t08', '.xdb', '.das', '.fro', '.np', '.npt', '.tax2008', '.otl', '.wea', '.gno', '.sqd', '.or6', '.vrd', '.t11', '.lix', '.brw', '.pd5', '.pspd', '.bjo', '.rou', '.pkh', '.epf', '.scd', '.xfdf', '.spv', '.ctf', '.mcd', '.ies', '.qfx', '.gan', '.isf', '.mph', '.qbw', '.sta', '.pod', '.qif', '.tax2019', '.mat', '.mdx', '.mmf', '.fxp', '.mdc', '.mw', '.dbd', '.phm', '.dal', '.ndk', '.wb3', '.ddcx', '.ftw', '.exp', '.tt10', '.tax2011', '.fmc', '.itmsp', '.pnproj', '.mbx', '.mws', '.hml', '.sle', '.vdx', '.mtw', '.esx', '.vi', '.epw', '.clm', '.sgml', '.xdna', '.gc', '.t09', '.npr', '.qdp', '.rod', '.liveupdate', '.pjm', '.tt12', '.ddc', '.igc', '.qb2012', '.bcc', '.flo', '.kpp', '.grr', '.shw', '.pxf', '.vtx', '.kid', '.lgh', '.ixb', '.opx', '.kpx', '.wnk', '.csa', '.zdc', '.lsl', '.dmsp', '.qb2009', '.ulz', '.fo', '.ond', '.fhc', '.tfa', '.spub', '.tet', '.tkfl', '.mbg', '.tpb', '.blb', '.lix', '.ctm', '.tt13', '.swk', '.txf', '.stp', '.tda', '.awg', '.itm', '.lw4', '.wb2', '.ivt'],
    "Database": ['.te', '.mar', '.nmoney', '.dtsx', '.gdb', '.teacher', '.itw', '.ddl', '.itdb', '.nyf', '.pdb', '.mdf', '.sqlitedb', '.db', '.fmpsl', '.accde', '.trm', '.fdb', '.musiclibrary', '.cdb', '.marshal', '.accdt', '.accdc', '.accft', '.sdx', '.oqy', '.tvdb', '.daschema', '.dbc', '.daconnections', '.dacpac', '.v12', '.udl', '.sqlite3', '.db', '.odb', '.pan', '.eco', '.his', '.alf', '.sis', '.temx', '.approj', '.trc', '.abs', '.sql', '.db3', '.db.crypt', '.$er', '.cpd', '.fil', '.4dl', '.nv2', '.dp1', '.rod', '.gdb', '.fic', '.fp3', '.btr', '.sqlite', '.crypt12', '.mdb', '.db.crypt12', '.cdb', '.qvd', '.p97', '.wmdb', '.dxl', '.db-wal', '.ask', '.dlis', '.fdb', '.px', '.dcb', '.musicdb', '.flexolibrary', '.mdw', '.hdb', '.fm', '.dbf', '.sdf', '.crypt8', '.fdb', '.dbs', '.usr', '.db.crypt8', '.accdb', '.frm', '.crypt15', '.xld', '.adp', '.crypt1', '.crypt7', '.pdm', '.mav', '.sdb', '.wdb', '.crypt9', '.db-journal', '.dsn', '.adf', '.fp7', '.crypt10', '.luminar', '.ibd', '.aq', '.exb', '.mmbak', '.ac', '.tnfp', '.pqa', '.dbx', '.sdc', '.orx', '.grdb', '.nnt', '.abx', '.mwb', '.crypt14', '.chck', '.sdb', '.edb', '.nsf', '.trc', '.crypt6', '.4dd', '.adb', '.fpt', '.maw', '.scx', '.mbtiles', '.kdb', '.ora', '.mpd', '.crypt', '.rpd', '.ndf', '.sdb', '.bak', '.crypt5', '.lgc', '.ihx', '.rodx', '.lwx', '.nwdb', '.ib', '.rmgc', '.cdb', '.maq', '.mdn', '.vvv', '.myd', '.db-shm', '.sdb', '.accdr', '.abcddb', '.udb', '.realm', '.fmp12', '.maf', '.cat', '.vis', '.qry', '.odb', '.pdb', '.tps', '.dad', '.sdy', '.db2', '.rctd', '.cma', '.mdbhtml', '.anb', '.tsd', '.dqy', '.caf', '.kexi', '.nrmlib', '.epim', '.trash_database', '.bacpac', '.ipj', '.xmlff', '.dbv', '.dcx', '.pnz', '.dbt', '.ade', '.mrg', '.ftb', '.sas7bdat', '.spq', '.idb', '.nv', '.accdw', '.ecx', '.sbf', '.mfd', '.fmp', '.jet', '.tmd', '.rsd', '.dsk', '.mdt', '.ckp', '.mud', '.adb', '.fp4', '.odl', '.ns2', '.dadiagrams', '.erx', '.rbf', '.mdz', '.fp5', '.^^^', '.wrk', '.fm5', '.bc3', '.adn', '.kexic', '.p96', '.vpd', '.xdb', '.jtx', '.owc', '.pvoc', '.dct', '.gwi', '.dab', '.sda', '.edb', '.tvdb', '.ns3', '.rod', '.icdb', '.odlsent', '.fkr', '.mas', '.kno', '.fol', '.ns4', '.fcd', '.kexis', '.r2d'],
    "Game": ['.u8', '.mii', '.sims3pack', '.osr', '.ttr', '.bns', '.usx', '.npa', '.w3n', '.ddt', '.kodu', '.vpk', '.gbx', '.pss', '.osz', '.pxp', '.sfar', '.mca', '.mgx', '.dek', '.rep', '.unity3d', '.p3t', '.sami', '.osk', '.ess', '.age3sav', '.scworld', '.zs9', '.sims3', '.bfs', '.wz', '.w3x', '.bzw', '.lrf', '.papa', '.mp2s', '.honmod', '.pcc', '.gma', '.gba', '.mcstructure', '.zs2', '.xom', '.isr', '.zs4', '.arch00', '.zs5', '.wtd', '.sii', '.gsc', '.rez', '.ydc', '.wld', '.xpd', '.mcworld', '.forge', '.v64', '.gcm', '.b', '.w3m', '.package', '.unr', '.mpm', '.ydr', '.mcr', '.nds', '.schematic', '.sc2assets', '.crp', '.mis', '.ain', '.xp3', '.dem', '.upk', '.wotreplay', '.dek', '.tbm', '.ycm', '.z4', '.gmres', '.menu', '.smrailroadssavedgame', '.z64', '.smc', '.age3scn', '.bmz', '.pck', '.esm', '.mp2m', '.gen', '.h4r', '.wad', '.scs', '.gbc', '.litemod', '.nar', '.lmu', '.sc2replay', '.tor', '.gdg', '.esp', '.uasset', '.unitypackage', '.scs', '.rvdata', '.cgz', '.ltx', '.3dsx', '.wowsreplay', '.zs0', '.pwf', '.am1', '.gb', '.bo2', '.bsp', '.nbs', '.bin', '.sc2save', '.pgn', '.lvl', '.plr', '.vdf', '.spc', '.save', '.dat_new', '.pak', '.sfo', '.mcserver', '.ct', '.dat', '.sc4', '.rvz', '.acww', '.n64', '.mcpack', '.sc2map', '.wad', '.dazip', '.age3ysav', '.vtf', '.big', '.w3g', '.aao', '.mdl', '.rep', '.vmf', '.grf', '.mpq', '.psv', '.sfc', '.nes', '.gam', '.pkg', '.3ds', '.cdp', '.bmd', '.wtf', '.pbp', '.pk3', '.kv3', '.ut4mod', '.rpl', '.s2z', '.sli', '.nltrack', '.ztmp', '.mrs', '.zs3', '.xs', '.bsa', '.saber', '.arp', '.rttex', '.age3xsav', '.sg0', '.mgl', '.frz', '.pqhero', '.stencyl', '.zs7', '.sc2ma', '.lsd', '.mae', '.sc4desc', '.sc2mod', '.vrcw', '.gms', '.sdz', '.luxb', '.dsg', '.masseffectsave', '.sc2archive', '.sha', '.lsl', '.idx0', '.pex', '.info', '.ff', '.bin', '.xpk', '.rgss3a', '.ipl', '.iwd', '.sav', '.sav', '.ttarch', '.spb', '.bin', '.sm', '.sims2pack', '.compiled', '.bps', '.splane', '.schem', '.mas', '.fuk', '.map', '.game', '.pup', '.tim', '.utx', '.blp', '.bar', '.fps', '.esp', '.world', '.jap', '.mahjongtitanssave-ms', '.qc', '.cgf', '.world', '.cpn', '.m2', '.nro', '.bif', '.sgm', '.uc', '.bfg', '.ba2', '.svs', '.rvdata2', '.vmv', '.md2', '.vol', '.bsb', '.usa', '.age3rec', '.vfs0', '.carc', '.esm', '.usm', '.xci', '.rgssad', '.w3z', '.rxdata', '.course', '.chd', '.mwl', '.fssave', '.sad', '.xmb', '.brf', '.wotbreplay', '.fomod', '.sid', '.wbt', '.fgd', '.lmp', '.scx', '.u', '.zs1', '.dek', '.wdb', '.wam', '.srm', '.dmb', '.project', '.cbv', '.hot', '.gbaskin', '.z3', '.ldw', '.jmf', '.ibt', '.dl', '.68k', '.eng', '.cxi', '.mstxt', '.nsz', '.bik', '.sqf', '.blz', '.udk', '.fml', '.ssc', '.sav', '.ydk', '.mcapm', '.ztd', '.scm', '.map', '.bus', '.far', '.rvproj', '.raw', '.xen', '.duc', '.age3xrec', '.gdi', '.world', '.ted', '.emd', '.rfm', '.lss', '.dm_83', '.csb', '.unityproj', '.dv2', '.sta', '.dif', '.pkx', '.ngage', '.brres', '.uxx', '.fcs', '.vcm', '.ips', '.sga', '.adt', '.zmap', '.wbax', '.phn', '.bls', '.ngp', '.gdshader', '.pssg', '.tiger', '.xnb', '.img', '.ukx', '.h3m', '.bgl', '.narc', '.0', '.wz', '.ut3', '.escape', '.fos', '.scx', '.zip', '.swc', '.stormreplay', '.pk4', '.ups', '.lgp', '.cbh', '.hum', '.ntrk', '.z2f', '.galaxy', '.smzip', '.001', '.dol', '.pod', '.gr2', '.pln', '.sc2bank', '.elf', '.nsbmd', '.fsm', '.omod', '.zst', '.gcf', '.umd', '.sgb', '.zs6', '.ovh', '.dec', '.age3yrec', '.pcsav', '.twt', '.ut2mod', '.unf', '.rom', '.chk', '.utc', '.blackhawkstriker2', '.h5u', '.bejeweled2deluxesavedgame', '.z5', '.clip', '.sc4lot', '.scn', '.vb', '.mgx', '.masseffectprofile', '.zblorb', '.player', '.ll', '.erf', '.hps', '.vob', '.love', '.dm2', '.shader', '.dun', '.qwd', '.asr', '.j2i', '.nca', '.bo3', '.j2l', '.maplet', '.wagame', '.mis', '.ns1', '.vmv', '.replay', '.pssl', '.dns', '.dnf', '.dem', '.sc2data', '.dm_82', '.fl', '.bme', '.radq', '.cty', '.md3', '.fpg', '.zds', '.g3x', '.prk', '.sgf', '.umod', '.bookwormdeluxesavedgame', '.mul', '.rgd', '.egm', '.esg', '.sgpbprj', '.fcm', '.gbcskin', '.dwi', '.idx255', '.gpf', '.lsw', '.fs2', '.gfx', '.sdt', '.vrmanifest', '.msproj', '.bms', '.plr', '.lip', '.wbox', '.fst', '.pbn', '.dm_84', '.blasterball3savedgame', '.playmission', '.kwreplay', '.puz', '.ctx', '.wu8', '.dmo', '.esl', '.ncf', '.sav', '.nsbtx', '.ecw', '.minesweepersave-ms', '.whirld', '.scn', '.jg4', '.nl2script', '.toc', '.soepsx', '.e2gm', '.sud', '.bnk', '.sprite', '.jst', '.zs8', '.ac', '.srl', '.sd7', '.blorb', '.uvx', '.cdp2', '.dwd', '.erb', '.rpgproject', '.wal', '.xds', '.sqm', '.ut2', '.nsbca'],
    "Development": ['.awk', '.appxbundle', '.unity', '.lgo', '.in', '.rbxl', '.kv', '.cs', '.sb', '.sb2', '.appx', '.ypr', '.kt', '.ipr', '.sb3', '.ino', '.rbxm', '.class', '.pyd', '.py', '.cpp', '.luc', '.c', '.gitattributes', '.gs', '.vbp', '.arsc', '.sc', '.has', '.tt', '.aidl', '.mm', '.gch', '.slogo', '.am4', '.ph', '.xq', '.caproj', '.md', '.lua', '.pas', '.asm', '.xap', '.b', '.pbg', '.resx', '.trx', '.resources', '.patch', '.gm81', '.swc', '.config', '.po', '.vdproj', '.mf', '.cc', '.java', '.csproj', '.pwn', '.suo', '.res', '.ocx', '.res', '.gmx', '.ise', '.gmk', '.ymp', '.swift', '.dex', '.smali', '.hpp', '.fs', '.capx', '.qpr', '.v12.suo', '.cod', '.def', '.sln', '.r', '.y', '.appxupload', '.cd', '.fbp', '.bbc', '.bet', '.yml', '.rb', '.mxml', '.pjx', '.bluej', '.rul', '.swd', '.so', '.aia', '.dtd', '.lisp', '.nuspec', '.entitlements', '.mpx', '.ccs', '.ane', '.bpl', '.dgml', '.hs', '.wdgt', '.ssi', '.xamlx', '.xcdatamodeld', '.pbxbtree', '.agi', '.dox', '.s', '.ml', '.au3', '.xsd', '.xt', '.xaml', '.mk', '.pb', '.ipr', '.proto', '.s19', '.ex', '.vcxproj', '.rc', '.pl', '.o', '.pbj', '.fxml', '.ctp', '.pyw', '.rpy', '.vb', '.h', '.hbs', '.d', '.w32', '.idb', '.tk', '.v', '.targets', '.mrt', '.as3proj', '.rexx', '.dproj', '.myapp', '.msix', '.yaml', '.w', '.l', '.twig', '.vbg', '.scc', '.fpm', '.rdlc', '.asc', '.4db', '.cxp', '.ads', '.sc', '.mo', '.csx', '.abc', '.nupkg', '.asi', '.iml', '.bas', '.jsfl', '.tlh', '.f', '.testsettings', '.pbxuser', '.dcp', '.csp', '.gm6', '.fxc', '.jspf', '.gsproj', '.gld', '.tpu', '.ftl', '.pas', '.ui', '.livecode', '.i', '.as', '.gitignore', '.sud', '.cls', '.am7', '.f90', '.vbx', '.mak', '.cp', '.framework', '.hh', '.apa', '.pbxproj', '.storyboard', '.kdevprj', '.idl', '.xcworkspace', '.kdevelop', '.dmd', '.plc', '.ipch', '.nib', '.vm', '.diff', '.cu', '.v', '.svn-base', '.m', '.inc', '.markdown', '.vhd', '.pika', '.as2proj', '.wiq', '.jic', '.autoplay', '.cbp', '.hal', '.sma', '.rsrc', '.alb', '.dpr', '.ism', '.asm', '.ist', '.wdl', '.nvv', '.prg', '.wdw', '.am6', '.pro', '.bsc', '.tur', '.xpp', '.fsscript', '.dsgm', '.lnt', '.clw', '.iconset', '.wdp', '.lds', '.lsproj', '.oca', '.haml', '.df1', '.mcp', '.wsc', '.sltng', '.ltb', '.bdsproj', '.rbc', '.for', '.pbk', '.erl', '.nls', '.m', '.wsp', '.sas', '.nsi', '.dbml', '.dpl', '.ilk', '.cxx', '.bb', '.pl1', '.xcconfig', '.octest', '.omo', '.nbc', '.pkgdef', '.gem', '.vbproj', '.kpl', '.sup', '.playground', '.m4', '.hxx', '.src', '.uml', '.pl', '.sym', '.cdf', '.mshc', '.xoml', '.mss', '.mshi', '.inl', '.v11.suo', '.xojo_xml_project', '.msha', '.ctxt', '.erb', '.owl', '.pcp', '.mer', '.cp', '.jpr', '.pyx', '.pxd', '.csi', '.exp', '.a2w', '.xojo_project', '.pm', '.wxl', '.vsmacros', '.edmx', '.forth', '.dm1', '.ccn', '.rss', '.dgsl', '.pli', '.nw', '.vdp', '.pri', '.mv', '.resw', '.asvf', '.nsh', '.wxs', '.t', '.lbi', '.ftn', '.dob', '.ptl', '.ppc', '.acd', '.mom', '.cbl', '.dec', '.hpf', '.vssscc', '.ss', '.caf', '.pot', '.a', '.tld', '.testrunconfig', '.xql', '.pkgundef', '.src.rpm', '.lxsproj', '.tmlanguage', '.textfactory', '.bbproject', '.ned', '.odl', '.wixlib', '.wixmst', '.vspx', '.xcodeproj', '.vsz', '.p3d', '.wixout', '.wixobj', '.xojo_menu', '.jcp', '.rav', '.neko', '.xcsnapshots', '.wdgtproj', '.pri', '.addin', '.vsps', '.bs2', '.resjson', '.xojo_binary_project', '.fbz7', '.dpkw', '.vtm', '.rex', '.fxl', '.rodl', '.vdm', '.licx', '.gmo', '.vspscc', '.ple', '.am5', '.cvsrc', '.vbz', '.rnc', '.iws', '.lucidsnippet', '.rbp', '.lbs', '.refresh', '.cob', '.gs3', '.ged', '.fsproj', '.bcp', '.dcuil', '.iwb', '.gorm', '.fxcproj', '.eql', '.mdzip', '.gszip', '.gameproj', '.scriptterminology', '.gemspec', '.rise', '.dbproj', '.tcl', '.wpw', '.xcappdata', '.pdm', '.tli', '.clips', '.tns', '.psc', '.vc', '.pch', '.ent', '.c', '.brx', '.idt', '.lproj', '.xcarchive', '.dba', '.greenfoot', '.licenses', '.4th', '.ctl', '.spec', '.dsp', '.edml', '.xib', '.vgc', '.fsproj', '.p', '.tds', '.mod', '.csn', '.vtv', '.bbprojectd', '.aps', '.dpk', '.r', '.msp', '.mpr', '.groupproj', '.prg', '.bpg', '.vsmdi', '.tu', '.fxpl', '.sqlproj', '.dcproj', '.vsmproj', '.rbw', '.xqm', '.vtml', '.inform', '.psm1', '.dbo', '.fsx', '.sdef', '.gfar', '.pde', '.lhs', '.wixproj', '.cfc', '.pod', '.vsp', '.exw', '.dcu', '.rkt', '.dfm', '.csi', '.ncb', '.msl', '.ccgame', '.sbproj', '.fsi', '.nqc', '.artproj', '.dbpro', '.dba', '.vcp', '.wxi', '.groovy', '.wixmsp', '.wixpdb', '.lit', '.magik', '.xquery', '.ssc', '.scriptsuite', '.deviceids', '.jpx', '.gmd', '.r'],
    "Backup": ['.abk', '.bkz', '.acp', '.wx', '.dsb', '.blend1', '.qbmb', '.vbox-prev', '.scripa', '.spg', '.jpa', '.bak2', '.sqb', '.onepkg', '.mbk', '.bdb', '.adi', '.arc', '.sis', '.spf', '.cbu', '.fbu', '.lcb', '.003', '.pvhd', '.rdb', '.sv2i', '.backup1', '.bak', '.dup0', '.smem', '.gbp', '.kb2', '.spass', '.wjf', '.ldabak', '.abu1', '.nba', '.tlg', '.nmm', '.dss', '.ba9', '.gho', '.bmk', '.bif', '.bff', '.v2i', '.fbf', '.fbw', '.tibx', '.bakx', '.fpsx', '.bak', '.sbb', '.abu', '.stg', '.orig', '.sdc', '.__a', '.bifx', '.sbu', '.sim', '.mbf', '.ck9', '.bps', '.jbk', '.csd', '.nbf', '.qic', '.vbm', '.paq', '.tmp', '.bkup', '.ipd', '.sna', '.backupdb', '.bak', '.walletx', '.da0', '.sn1', '.ate', '.srr', '.bpa', '.blend2', '.mig', '.rmbak', '.mdinfo', '.win', '.ba6', '.nco', '.skb', '.old', '.spi', '.pbd', '.sv$', '.asd', '.as4', '.afi', '.ful', '.tig', '.ati', '.bak~', '.bookexport', '.ba8', '.ba7', '.nrs', '.dpb', '.inprogress', '.$db', '.csm', '.rbs', '.backup.metadata', '.adi', '.nbf', '.pfi', '.enc', '.vpcbackup', '.npf', '.abbu', '.bak3', '.cbk', '.fbk', '.kmnb', '.backup', '.bkf', '.gb1', '.001', '.bck', '.bpn', '.sav', '.dbk', '.$$$', '.bac', '.llx', '.nbu', '.nbk', '.tini', '.snmm', '.ba0', '.obk', '.abf', '.ccctask', '.imazingapp', '.imazing', '.dim', '.mddata', '.qba.tlg', '.bcm', '.dash', '.vrb', '.jps', '.wbb', '.aqz', '.qbx', '.fh', '.bak', '.tmp', '.mem', '.bup', '.noy', '.dbk', '.qsf', '.bpm', '.rbf', '.bak', '.wbk', '.ab', '.arc', '.ibk', '.tdb', '.qualsoftcode', '.bkp', '.bak', '.crds', '.win', '.vbk', '.pbx5script', '.bm3', '.trn', '.sn2', '.mdbackup', '.dov', '.bkc', '.wbx', '.tbk', '.ghs', '.gs-bck', '.lbf', '.win', '.pdb', '.ptb', '.wbcat', '.quicken2017backup', '.fza', '.asvx', '.113', '.qbm', '.bkp', '.bckp', '.w01', '.mpb', '.xlk', '.gb2', '.pbf', '.nbak', '.bk1', '.flka', '.bbb', '.fwbackup', '.aea', '.nda', '.uci', '.qbmd', '.cenon~', '.nps', '.quicken2015backup', '.rbf', '.tibkp', '.fbc', '.ebabackup', '.rdb', '.iv2i', '.vmsg', '.ftmb', '.bk1', '.aba', '.nbd', '.bkp', '.nbk', '.jwlibrary', '.quicken2016backup', '.prv', '.sps', '.fhf', '.tmr', '.nfb', '.73b', '.nfc', '.bk', '.pbf', '.exml', '.bpb', '.acr', '.sme', '.jdc', '.yrcbck', '.asv', '.xbk', '.tis', '.pbb', '.nbs', '.pqb', '.nmmm', '.ori', '.nbd', '.bbz', '.nbi', '.ashbak', '.flkb', '.qv~', '.oeb', '.cmf', '.dna', '.qbk', '.mynotesbackup', '.__b', '.qbb', '.nb7', '.vpb', '.nwbak', '.wspak', '.~cw', '.oyx', '.@@@', '.caa', '.sns', '.wpb', '.cbs', '.diy', '.mabk', '.fbk', '.mbw', '.pdu', '.rbf', '.rbc', '.pvc', '.pbj', '.mv_', '.pqb-backup', '.2fas', '.zbfx', '.safenotebackup', '.dba', '.mbk', '.icbu', '.yoti', '.abex', '.ofbr', '.pbxscript', '.ba1', '.bpk', '.orrs', '.nrbak', '.ttbk', '.rrr', '.sbs', '.msim', '.icf', '.rbk', '.quickenbackup', '.pba', '.sall', '.fzb', '.psa', '.rmgb', '.j01', '.obk', '.scbackup'],
    "Web": ['.key', '.scss', '.mjs', '.ssp', '.btapp', '.aro', '.asax', '.xd', '.xhtm', '.p7b', '.a5w', '.bml', '.jspa', '.vrt', '.dll', '.php', '.whtt', '.cshtml', '.dhtml', '.website', '.download', '.crt', '.xul', '.js', '.obml15', '.webbookmark', '.rjs', '.vsdisco', '.mml', '.p7', '.fwtemplate', '.p7c', '.ascx', '.h5p', '.dcr', '.css', '.zul', '.dochtml', '.spc', '.pac', '.htaccess', '.tpl', '.site', '.a4p', '.pem', '.aspx', '.seam', '.json', '.kit', '.appcache', '.svr', '.shtml', '.dwt', '.dap', '.url', '.oam', '.wbs', '.htc', '.htm', '.pro', '.gsp', '.asr', '.wsdl', '.obml16', '.chat', '.gne', '.master', '.disco', '.gsp', '.public', '.fwp', '.epibrw', '.rw3', '.xpd', '.strm', '.chm', '.p12', '.ap', '.asp', '.axd', '.webmanifest', '.php4', '.sites2', '.bok', '.php2', '.vdw', '.obml', '.xss', '.br', '.der', '.phtml', '.nzb', '.mhtml', '.con', '.rhtml', '.ashx', '.web', '.opml', '.har', '.rss', '.html', '.do', '.olp', '.asa', '.hyperesources', '.browser', '.cms', '.razor', '.aex', '.alx', '.edge', '.sparkle', '.duckload', '.sht', '.cha', '.qf', '.srf', '.sdb', '.jnlp', '.crl', '.fmp', '.pptmhtml', '.stc', '.csr', '.node', '.uhtml', '.xbel', '.wdgt', '.xfdl', '.jsp', '.fwtemplateb', '.ewp', '.zhtml', '.stml', '.webloc', '.page', '.dbm', '.shtm', '.cfm', '.awm', '.mht', '.dothtml', '.compressed', '.wml', '.cer', '.xht', '.jspx', '.psp', '.dml', '.jss', '.tpl', '.sitemap', '.itms', '.ucf', '.wpp', '.jsonl', '.vbd', '.vrml', '.ndjson', '.discomap', '.sass', '.maff', '.hxs', '.csp', '.hype', '.xhtml', '.jhtml', '.hdml', '.xws', '.rt', '.svc', '.pub', '.zhtml', '.hypetemplate', '.prf', '.phtm', '.adr', '.sites', '.htx', '.muse', '.mjml', '.hypesymbol', '.esproj', '.srl', '.stl', '.wbn', '.wkdownload', '.gmi', '.zvz', '.wbxml', '.vbhtml', '.iqy', '.ognc', '.fwtb', '.codasite', '.webarchive', '.qbo', '.ece', '.docmhtml', '.mspx', '.nod', '.woa', '.wgp', '.mvc', '.lasso', '.xbl', '.zfo', '.freeway', '.oth', '.lbc', '.idc', '.att', '.php3', '.tvvi', '.webhistory', '.webarchivexml', '.widget', '.asmx', '.swz', '.map', '.bwp', '.mapx', '.jws', '.itpc', '.atom', '.tvpi', '.cdf', '.html.mem', '.faces', '.wgt', '.hdm', '.rwsw', '.rflw', '.php5', '.mvr', '.rwp', '.vlp', '.stp', '.ptw', '.nxg', '.ccbjs', '.saveddeck', '.qrm', '.an', '.wn', '.ppthtml', '.stm', '.less', '.json5', '.iwdgt', '.suck', '.private', '.jcz', '.cfml', '.jst', '.cpg', '.wpx', '.rwtheme', '.jvs', '.cphd', '.qbx', '.kcmsf', '.moz', '.fcgi', '.nojekyll'],
    "GIS": ['.gmap', '.nm2', '.sp3', '.sbn', '.ssf', '.dt0', '.wlx', '.wor', '.qgs', '.jnx', '.apl', '.mxt', '.avl', '.div', '.3d', '.mpk', '.dem', '.saf', '.3dl', '.ptm', '.gst', '.embr', '.osm', '.dt1', '.gsm', '.tfrd', '.pmf', '.atx', '.osc', '.gml', '.fmw', '.cxf', '.mif', '.bt', '.kmz', '.hdr', '.mxd', '.sdf', '.timestamp', '.msd', '.dix', '.3dc', '.kml', '.obf', '.lan', '.csf', '.nmf', '.fbl', '.aux', '.gprx', '.prm', '.qpj', '.gvsp', '.e00', '.len', '.dmt', '.grb', '.pyt', '.gsi', '.geojson', '.nmc', '.pix', '.hgt', '.ref', '.qgz', '.wld', '.adf', '.imi', '.rdf', '.gsr', '.glb', '.tab', '.gpx', '.aqm', '.rdc', '.gps', '.dmf', '.imd', '.svx', '.vdc', '.rmp', '.vct', '.mwx', '.sbn', '.gsb', '.style', '.mmm', '.mid', '.jgw', '.rgn', '.axe', '.cub', '.fit', '.sxd', '.usr', '.sdw', '.xol', '.tfw', '.jpw', '.shp', '.sgy', '.mps', '.ptt', '.dlg', '.eta', '.stt', '.qlv', '.fmi', '.fme', '.mdc', '.lpk', '.3dd', '.sld', '.img', '.ttkgp', '.gmf', '.ov2', '.ocd', '.segy', '.mwm', '.vec', '.fds', '.mmz', '.nm7', '.gpkg', '.pin', '.nv2', '.img', '.th', '.jpgw', '.ers', '.tcx', '.bil', '.at5', '.dt2', '.ngt', '.477', '.smp', '.est', '.smm', '.qrt', '.mnh', '.osb', '.nm3', '.nmap', '.apr', '.ffs', '.map', '.rst', '.fls', '.fmv', '.tpx', '.gtm', '.rrd', '.map', '.wkt', '.svp', '.anz', '.sym', '.aqx', '.trb', '.gpf', '.cvi', '.mgm', '.axt', '.sbf', '.gsr2', '.cml', '.qct', '.gws', '.sxf', '.bpw', '.jpr', '.sdm', '.gfw', '.cor', '.wfd', '.dvc'],
    "Disk": ['.dmg', '.cso', '.iso', '.vfd', '.mds', '.dvd', '.img', '.vmdk', '.rom', '.mdf', '.vdi', '.dsk', '.i02', '.lvi', '.wlz', '.cfs', '.ashdisc', '.dbr', '.mbi', '.vaporcd', '.bws', '.d64', '.macvm', '.ex01', '.d01', '.dmgpart', '.vhd', '.l01', '.bin', '.daa', '.xvd', '.cif', '.d00', '.sdi', '.md0', '.qcow', '.lcd', '.mdx', '.qcow2', '.nrg', '.hdi', '.avhd', '.dcf', '.sub', '.vmwarevm', '.ibp', '.iso', '.wim', '.vhdx', '.toast', '.uibak', '.xva', '.bif', '.e01', '.hds', '.i01', '.bwt', '.ima', '.wud', '.tib', '.cdt', '.cdm', '.ccd', '.ecm', '.xdi', '.sdsk', '.ede', '.adz', '.dax', '.vc4', '.isz', '.ipf', '.img', '.cdi', '.2mg', '.vcd', '.img', '.cdr', '.uif', '.adf', '.eui', '.md1', '.sqfs', '.bwi', '.disk', '.gcd', '.sco', '.dvdr', '.flp', '.mrimg', '.mfi', '.hfs', '.p01', '.vcd', '.swm', '.omg', '.pvm', '.hc', '.ndif', '.tc', '.tap', '.tzx', '.000', '.mlc', '.b5i', '.utm', '.lx01', '.bdf', '.gbi', '.x64', '.toc', '.udf', '.edk', '.st', '.fdi', '.rcl', '.flg', '.t64', '.fdd', '.imd', '.b6i', '.aff', '.i00', '.smi', '.image', '.cue', '.gkh', '.sparseimage', '.bwz', '.cl5', '.md1', '.partimg', '.md2', '.afd', '.bwa', '.p01', '.hdd', '.woz', '.pgd', '.ciso', '.pmf', '.ixa', '.vco', '.vcx', '.pxi', '.image', '.ibadr', '.wmt', '.pqi', '.xa', '.vdi', '.hfv', '.p2g', '.gi', '.nkit', '.nn', '.disc', '.rdf', '.pdi', '.wii', '.dms', '.ibq', '.c2d', '.ibb', '.eda', '.imz', '.wbi', '.dxp', '.gdrive', '.cd', '.b5t', '.86f', '.td0', '.b6t', '.edv', '.simg', '.hd', '.atr', '.miniso', '.winclone', '.volarchive', '.sopt', '.lnx', '.g41', '.adf', '.sparsebundle', '.ncd', '.xmd', '.p2i', '.fcd', '.mir', '.nfi', '.ratdvd', '.edq', '.wil', '.rpkg', '.fd', '.qed', '.do', '.po', '.afm', '.d81', '.pgx', '.d71', '.vhdpmem', '.raw', '.d88', '.ddi', '.tao', '.dao', '.vc8', '.eds', '.vc6', '.xmf', '.ibdat', '.aa', '.ufs', '.k3b', '.tap'],
    "CAD": ['.cir', '.bak', '.axm', '.bdc', '.psm', '.iba', '.dlv', '.smb', '.epf', '.sim', '.cpa', '.afs', '.opt', '.tct', '.mp12', '.mcx', '.pat', '.jt', '.gsm', '.edf', '.db1', '.fpc', '.psv', '.mc9', '.rtd', '.jvsg', '.dsnx', '.lcf', '.cad', '.gds', '.catproduct', '.job', '.gcode', '.model', '.logicly', '.cyp', '.3dl', '.lin', '.ide', '.adi', '.dra', '.nc', '.vet', '.asy', '.mto', '.dc3', '.rsg', '.cad', '.cib', '.li3d', '.ms14', '.msm', '.afd', '.fcstd1', '.pc7', '.dwt', '.terx', '.sat', '.123dx', '.des', '.pss', '.skf', '.ms13', '.xv3', '.dst', '.mhs', '.pwt', '.jvsgz', '.edn', '.dsn', '.pln', '.spt', '.sldasm', '.icd', '.sldprt', '.blk', '.dru', '.fzb', '.phj', '.cf2', '.nwf', '.bcd', '.fzp', '.dc2', '.nc', '.123d', '.iso', '.cff', '.mp11', '.mp10', '.min', '.cgr', '.dwfx', '.stl', '.igs', '.mde', '.idv', '.pla', '.dws', '.asm', '.fcw', '.dc1', '.tc2', '.xnc', '.isoz', '.dgn', '.easm', '.ldr', '.prg', '.scad', '.jam', '.stp', '.x_b', '.mp7', '.bmf', '.shx', '.vwx', '.bdl', '.ics', '.rig', '.sch', '.rsm', '.fmz', '.svd', '.if', '.czd', '.prt', '.fzz', '.art', '.cdw', '.sch', '.fz', '.prt', '.dwg', '.unt', '.hsc', '.wdf', '.bbcd', '.cyp', '.any', '.ltl', '.act', '.gxm', '.libpkg', '.sab', '.tsf', '.modfem', '.circuit', '.123', '.dfx', '.cam', '.gxc', '.drw', '.ezd', '.plush', '.step', '.dxf', '.asc', '.mcd', '.catpart', '.prt', '.g', '.tak', '.nc1', '.psf', '.jbc', '.rra', '.dxx', '.cdl', '.bpm', '.ipt', '.catdrawing', '.tcd', '.fcstd', '.ewb', '.xise', '.wdp', '.cnc', '.iam', '.dgk', '.dxe', '.dsnwrk', '.g3d', '.xbf', '.lizd', '.red', '.ezp', '.tcm', '.eld', '.uld', '.fnc', '.ard', '.opj', '.ngc', '.cam', '.dlx', '.topviw', '.sew', '.idw', '.ldt', '.plp', '.dc', '.slddrw', '.olb', '.a2l', '.ipn', '.123c', '.cnc', '.rdf', '.drwdot', '.hsf', '.tsc', '.drg', '.bxl', '.gcd', '.2d', '.min', '.pho', '.fpd', '.prt', '.geo', '.brd', '.ms11', '.bit', '.dcd', '.brd', '.pm3', '.neu', '.3w', '.mp13', '.brep', '.dft', '.ic3d', '.ifcxml', '.npl', '.dgb', '.pc6', '.bpmc', '.prtdot', '.ewd', '.tc3', '.hus', '.tcd', '.scdoc', '.ginspect_prj', '.fzbz', '.lia', '.ms12', '.ipf', '.lay6', '.cddx', '.fan', '.eprt', '.asmdot', '.smt', '.logiclylib', '.mfp', '.t3001', '.easmx', '.sza', '.adt', '.schdoc', '.lfview', '.vds', '.eqn', '.mmg', '.g', '.tgi', '.wbt', '.rcm', '.x_t', '.nwd', '.exb', '.ipj', '.crv', '.nwc', '.vnd', '.pro', '.mp14', '.lyr', '.pipe', '.bimx', '.tcw', '.gxd', '.drw', '.rcd', '.gx', '.tbp', '.psu', '.flx', '.vtf', '.tcp', '.cmp', '.mvs', '.mdl', '.ngd', '.rml', '.dvg', '.lyc', '.tcx', '.kit', '.sch', '.tpl', '.pcs', '.edrw', '.prjpcb', '.topprj', '.att', '.ise', '.dra', '.3dc', '.cnd', '.sym', '.dbq', '.mp8', '.top', '.rs', '.ckd', '.sdg', '.sbp', '.gbx', '.smg', '.bsw', '.ppa', '.bbcdx', '.plc', '.ezc', '.iqp', '.pbb', '.fm', '.fzm', '.ms7', '.bswx', '.pipd', '.pwd', '.qpm', '.l3b', '.fpp', '.ms9', '.mp9', '.rcv', '.sch', '.idcl', '.ckt', '.dxo', '.prjmbd', '.prjscr', '.cyg', '.ad_prt', '.bpz', '.gxh', '.mod', '.dsg', '.ifczip', '.dc2', '.sst', '.hcp', '.upf', '.cel', '.mod', '.cmp', '.fcd', '.pca'],
    "Plugin": ['.aplg', '.amxx', '.milk', '.asi', '.ccip', '.rez', '.dlr', '.tpi', '.rpln', '.scm', '.rbz', '.tgp', '.acroplugin', '.bav', '.cleo', '.amx', '.lng', '.mda', '.crx', '.ecf', '.oiv', '.vbox-extpack', '.mde', '.zxp', '.fb2k-component', '.inx', '.alp', '.eaz', '.sparc', '.rwplugin', '.8bi8', '.assetproj', '.avx', '.dlo', '.skypechatstyle', '.ny', '.aaxplugin', '.8bx', '.8bi', '.plgx', '.xpi', '.flt', '.vst', '.oex', '.vsix', '.wlz', '.nbm', '.aex', '.blu', '.xpt', '.8bf', '.api', '.prm', '.8bf', '.8ba', '.module', '.accdu', '.vdf', '.safariextz', '.info', '.plw', '.bundle', '.qtx', '.fzip', '.x32', '.xlv', '.hvpl', '.iadpage', '.aplp', '.xsiaddon', '.bkz', '.vst3', '.8li', '.oxt', '.plugin', '.aip', '.rpm', '.mxaddon', '.lng', '.wll', '.avx', '.xlam', '.fsb', '.tko', '.net', '.plugin', '.jsxbin', '.p64', '.agmodule', '.bmi', '.mdimporter', '.cmp', '.xll', '.m3p', '.rhp', '.qlplugin', '.accda', '.s4dix', '.seplugin', '.xmd', '.pim', '.apd', '.aix', '.mxp', '.8be', '.brm', '.aaui', '.fxt', '.ppam', '.ppa', '.fwaction', '.nbp', '.dlu', '.apl', '.8by', '.ibplugin', '.mmip', '.dpm', '.arx', '.sublime-package', '.fmx', '.vsl', '.component', '.pfl', '.mll', '.mfx', '.mtx', '.kmm', '.8bs', '.spe', '.ext', '.dbx', '.q1q', '.ebaplugin', '.rock', '.ape', '.t3x', '.pln', '.vdplugin', '.8bc', '.apext', '.8bl', '.flt', '.zpi', '.rplib', '.rxt', '.aseprite-extension', '.bzplug', '.nvda-addon', '.mltbx', '.fwactionb', '.tmbundle', '.bblm', '.plg', '.fmplugin', '.lrplugin', '.dfp', '.mode', '.qtr', '.plx64', '.osax', '.spd', '.indesignplugin', '.xla', '.ppmod', '.fs', '.aba', '.xba', '.addon', '.qar', '.fpi', '.iadstyle', '.q2q', '.sugar', '.codaplugin', '.wbm', '.pset', '.p', '.iadcomponent', '.zlb', '.q8r', '.m2p', '.mox', '.ccx', '.lrmodule', '.bro', '.plx', '.cst', '.xcodeplugin', '.ideplugin', '.qlgenerator', '.cvt', '.q9r', '.qpx', '.so-abi', '.dvtplugin', '.abi', '.luac', '.epk2', '.colorpicker', '.xnt', '.sa9', '.pba', '.bri', '.tbp', '.q5r', '.atx', '.iadclass', '.fzp', '.aseprite-data', '.iadaction', '.iadplug', '.afzplug', '.xcplugin', '.lrwebengine', '.dmkit', '.wowsl', '.syn', '.xadd', '.rpi', '.rev', '.cox', '.mpe1', '.wie', '.mat', '.mfw', '.exv', '.q9s', '.q7q', '.arpack', '.q4q'],
    "Miscellaneous": ['.adi', '.cbds', '.brushset', '.aawdef', '.ipsw', '.downloading', '.sr0', '.pdpcomp', '.sis.dm', '.t$m', '.isn', '.crdownload', '.dct', '.torrent', '.aod', '.msu', '.info', '.hxe', '.desktop', '.loov', '.zvpl', '.dtapart', '.partial', '.ldb', '.tfil', '.p10', '.bp3', '.opdownload', '.idlk', '.msf', '.gta', '.esd', '.search-ms', '.avastlic', '.bnd', '.info', '.jad', '.mtd', '._eml', '.lrc', '.sfv', '.fb!', '.part', '.mpcpl', '.mobileprovision', '.nth', '.lock', '.unknown', '.dat', '.nwp', '.vbt', '.3dc', '.tpm', '.ef2', '.rfp', '.vp3', '.ezw', '.rfn', '.pad', '.mls', '.inlk', '.cul', '.art80', '.growlregdict', '.xlnk', '.mgt', '.svn-work', '.nar', '.fpfv', '.sslf', '.ssd', '.glink', '.efl', '.snf', '.icma', '.chw', '.skba', '.xwf', '.inetloc', '.ltf', '.auz', '.id', '.!ut', '.dat', '.rov', '.sis', '.rwz', '.egt', '.ob!', '.olb', '.db', '.frm', '.cls', '.pla', '.gg', '.gp4', '.rtm', '.adadownload', '.ttx', '.jmx', '.sst', '.psw', '.g3a', '.cvr', '.fla', '.bbl', '.ocr', '.rsa', '.chk', '.sisx', '.mdl', '.bfc', '.cache', '.skr', '.drc', '.gsp', '.mvi', '.!bt', '.dat', '.tdl', '.p2p', '.tec', '.sec', '.appup', '._nws', '.psi', '.slf', '.td', '.unl', '.bc', '.md5', '.file', '.wba', '.dlm', '.bup', '.csh', '.pvk', '.zml', '.wjf', '.fdr', '.rml', '.vncloc', '.apf', '.err', '.jqz', '.appdownload', '.gdraw', '.rnd', '.msi', '.crd', '.odf', '.wtc', '.bps', '.sdr', '.key', '.cfs', '.khd', '.ztf', '.tnef', '.arr', '.clkk', '.calibre', '.acl', '.cos2', '.sisx.dm', '.mthd', '.pamp', '.000', '.cxf', '.diskdefines', '.shs', '.tpl', '.nup', '.bc!', '.qua', '.sdx', '.hex', '.sig', '.dwl', '.crc', '.pes', '.wlx', '.vol', '.xslic', '.toc', '.pth', '.na2', '.plsk', '.plf', '.flf', '.rjs', '.mrk', '.abr', '.vmg', '.scw', '.xmp', '.exp', '.dbx', '.thm', '.mdf', '.lic', '.zm1', '.sft', '.z80', '.jmt', '.req', '.hs', '.ifl', '.vbt', '.fnd', '.hxk', '.jc!', '.mnl', '.dap', '.xsd', '.sc', '.enf', '.cl', '.mgo', '.clkx', '.lay', '.icalendar', '.pls', '.snm', '.wdseml', '.ics', '.erl', '.lid', '.zzz', '.manifest', '.mar', '.aria2', '.zm3', '.mat', '.ctg', '.xxx', '.vir', '.nomedia', '.ass', '.bt!', '.logonxp', '.rpmsg', '.dst', '.bst', '.cvf', '.jms', '.ost', '.cas', '.ing', '.bqy', '.exd', '.rtc', '.smwt', '.swj', '.sidd', '.dic', '.cds', '.83p', '.sidn', '.cfl', '.nk2', '.pando', '.tstream', '.fmelic', '.vor', '.chunk001', '.bootskin', '.mif', '.dwlibrary', '.xnk', '.mgdatabase', '.lxa', '.spk', '.swp', '.snt', '.spd', '.njb', '.hlx', '.lck', '.mso', '.cdf-ms', '.box', '.msrcincident', '.temp', '.ical', '.cp3', '.mmo', '.tip', '.wwd', '.aif', '.lyr', '.8xp', '.vmf_autosave', '.link', '.gau', '.zm2', '._sys.lfo', '.tls', '.rnd', '.w', '.dsc', '.flk', '.montage', '.aepkey', '.add', '.z1', '.rxc', '.crd', '.req', '.ppk', '.sk', '.jc', '.cch', '.kwm', '.fw', '.upg', '.decrypt', '.mta', '.shx', '.p7m', '.mzz', '.khi', '.mc2', '.icontainer', '.ssc', '.nav2', '.linx', '.imapmbox', '.skindex', '.sha512', '.enml', '.inca', '.ftploc', '.tpm', '.god', '.xol', '.lwtp', '.dstudio', '.sth', '.zci', '.art70', '.bpdx', '.logonvista', '.tldr', '.cnv', '.mtf', '.freakshow', '.cdsz', '.bws', '.bkmk', '.dr', '.mnx', '.kyr', '.az!', '.tlb', '.duid', '.mfil', '.rwlibrary', '.wje', '.clkw', '.jcw', '.pekey', '.cml', '.contour', '.vpc7', '.alt', '.ahi', '.p7r', '.hmx', '.vp4', '.mb', '.ptm', '.mjdoc', '.ext', '.mab', '.art', '.qds', '.nss', '.pkpass', '.vfs', '.mag', '.mcfp', '.tnsp', '.reloc', '.nfs', '.split', '.tbs', '.edc', '.mbs', '.mbb', '.vpa', '.dctmp', '.sum', '.bmk', '.dcover', '.letter', '.nick', '.pgp', '.mso', '.sxm', '.uls', '.psar', '.weavelibrary', '.ac$', '.hxa', '.jcl', '.disabled', '.imy', '.dhv', '.feedback', '.yps', '.blf', '.avgdx', '.rft', '.pvm', '.bli', '.ptr', '.licensekey', '.dal', '.itc', '.ncw', '.afploc', '.wrts', '.mwf', '.ssw', '.storymill', '.dwc', '.vpc6', '.ebn', '.tpkey', '.clkt', '.aml', '.dtf', '.slupkg-ms', '.clr', '.jrs', '.shv', '.shortcut', '.qxl', '.cerber3', '.map', '.ndl', '.mco', '.rmf', '.pn', '.dwn', '.in', '.slb', '.sbc', '.acb', '.ctf', '.indk', '.looklibrary', '.mwlic', '.lwk', '.raskinlicense', '.dek', '.wordlist', '.ybd', '.dmx-info', '.mailtoloc', '.kmr', '.vmdk-converttmp', '.cdlx', '.ztr', '.lrs', '.smrd', '.chksplit', '.ahd', '.rfb', '.xensearch', '.mcfi', '.sidb', '.merlinlicense', '.rmh', '.da2', '.sc2locale', '.aoi', '.mailplanelicense', '.papers', '.ntf', '.xpr', '.hdk', '.rat', '.ctf', '.hyp', '.ezlog', '.wzmul', '.rfc', '.fnlf', '.hxt', '.stmb', '.vmhr', '.otc', '.mxn', '.cdl', '.vmhf', '.radiumkey2', '.tcr', '.mcf'],
    "Encoded": ['.bhx', '.kde', '.ecd', '.rzk', '.vlt', '.pack', '.suf', '.gxk', '.filebolt', '.c9r', '.sef', '.cng', '.bpk', '.lastlogin', '.snk', '.blower', '.acid', '.cpio', '.atsofts', '.axx', '.scb', '.rap', '.locker', '.qewe', '.dco', '.kk', '.bcup', '.adame', '.enx', '.gdcb', '.bfa', '.pxf', '.odin', '.r2u', '.asc', '.gpg', '.bin', '.rem', '.bpw', '.tar.md5', '.efu', '.jceks', '.cuid2', '.zps', '.cpt', '.plp', '.poop', '.pcv', '.signature', '.safe', '.meo', '.sdtid', '.micro', '.bit', '.nc', '.film', '.bca', '.cryptra', '.fc', '.nxl', '.stxt', '.scb', '.ddoc', '.xtbl', '.cerber2', '.mjd', '.apkm', '.sdoc', '.enc', '.rsdf', '.krab', '.hqx', '.pwv', '.uu', '.cdoc', '.wolf', '.mme', '.uue', '.vp', '.hoop', '.sia', '.ded', '.salma', '.merry', '.viivo', '.zip.enc', '.ufr', '.k3y', '.jmc', '.srf', '.dcf', '.pyenc', '.uiwix', '.eoc', '.mse', '.b2a', '.seb', '.crypt', '.edoc', '.pdc', '.xxx', '.jks', '.aes', '.bsk', '.lcn', '.eslock', '.null', '.xmdx', '.vdata', '.xxe', '.efdc', '.ykcol', '.locked', '.jac', '.azs', '.sxls', '.cerber', '.psw6', '.coot', '.crypto', '.fgsf', '.mim', '.crypt1', '.mnc', '.pdex', '.encrypted', '.hid', '.sfi', '.kode', '.dime', '.dc4', '.spdf', '.emc', '.mime', '.keystore', '.dm', '.hid2', '.crypted', '.wnry', '.idea', '.esf', '.gfe', '.afp', '.dlc', '.pfile', '.sjpg', '.wlu', '.aurora', '.wallet', '.wrypt', '.jmce', '.nbes', '.r5a', '.fpenc', '.lilith', '.jmcx', '.sdo', '.aep', '.cef', '.ync', '.wpe', '.pdy', '.bfe', '.ccf', '.shy', '.codercrypt', '.xef', '.##', '.htpasswd', '.bip', '.jcrypt', '.ptrz', '.ryk', '.efr', '.wiot', '.spd', '.dim', '.gero', '.elbie', '.sspq', '.kifr', '.nitz', '.tcvp', '.nmo', '.eegf', '.eewt', '.eiur', '.edfw', '.maas', '.djvu', '.wrui', '.conti', '.wncry', '.sa', '.ksd', '.ppdf', '.mfs', '.zzzzz', '.mtzu', '.dcd', '.sgz', '.good', '.rdi', '.ssoi', '.uud', '.werd', '.paradise', '.adobe', '.pfo', '.zepto', '.pkey', '.hex', '.kxx', '.klq', '.bvd', '.chml', '.efl', '.repp', '.enx', '.mcrp', '.rzx', '.jmck', '.switch', '.cgp', '.lucy', '.exc', '.lvivt', '.wls', '.locky', '.kkk', '.yenc', '.e4a', '.fun', '.sme', '.iwa', '.vtym', '.bc5b', '.purge', '.cadq', '.jmcr', '.pxx', '.uea', '.ppenc', '.rrbb', '.u2k', '.medusa', '.sf', '.kcxz', '.sdfi', '.rensenware', '.efji', '.devos', '.mcq', '.lilocked', '.sage', '.fsm', '.mba', '.gzquar', '.qscx', '.dharma', '.litar', '.jmcp', '.stop', '.ctbl', '.sqz', '.wncryt', '.fonix', '.clx', '.lqqw', '.rcrypted', '.rumba', '.radman', '.sle', '.djvus', '.aze', '.sef', '.ks', '.btoa', '.voom', '.givemenitro', '.cuid', '.carote', '.sxml', '.wcry', '.azf', '.aaa', '.extr', '.hbx', '.mkf', '.lxv'],
    "Compressed": ['.mint', '.b6z', '.zst', '.apz', '.fzpz', '.sy_', '.sfg', '.xapk', '.rar', '.gzip', '.pkg.tar.xz', '.pup', '.tzst', '.tpsr', '.cit', '.s00', '.npk', '.pkg', '.deb', '.tar.xz', '.tbz', '.mpkg', '.7z', '.sit', '.bz2', '.pf', '.bndl', '.dz', '.001', '.ufs.uzip', '.qda', '.cbt', '.hbe', '.ice', '.ita', '.ecs', '.tbz2', '.cb7', '.sqx', '.lzm', '.lpkg', '.pa', '.gza', '.htmi', '.r2', '.pit', '.arduboy', '.dar', '.p7z', '.smpf', '.zpi', '.archiver', '.ecar', '.vrpackage', '.xopp', '.s7z', '.comppkg.hauptwerk.rar', '.ayt', '.ctx', '.xip', '.opk', '.dl_', '.par', '.cbr', '.b1', '.jsonlz4', '.uha', '.7z.002', '.002', '.zip', '.lemon', '.r00', '.cbz', '.taz', '.wa', '.pwa', '.rev', '.vip', '.f', '.nex', '.kgb', '.tar.gz', '.epi', '.sfx', '.q', '.zl', '.wick', '.pak', '.pcv', '.a02', '.ba', '.rpm', '.cdz', '.c00', '.apk', '.ari', '.zix', '.hki', '.tx_', '.par2', '.lz4', '.czip', '.tar.lz', '.apex', '.ar', '.whl', '.rte', '.7z.001', '.bundle', '.gz', '.ark', '.lz', '.c10', '.lzma', '.warc', '.sfs', '.kextraction', '.a01', '.ipk', '.rz', '.bz', '.bh', '.sitx', '.gmz', '.memo', '.spd', '.ace', '.z03', '.arc', '.r01', '.cxarchive', '.sdc', '.f3z', '.jar.pack', '.piz', '.sifz', '.spa', '.pea', '.cba', '.wastickers', '.xz', '.sdocx', '.fdp', '.war', '.xx', '.z', '.package', '.sh', '.tgs', '.sdoc', '.snb', '.0', '.shar', '.s02', '.oz', '.voca', '.004', '.gca', '.ctz', '.zz', '.ubz', '.r03', '.zpaq', '.p19', '.oar', '.pkz', '.sfm', '.zipx', '.a00', '.dd', '.r30', '.r0', '.c01', '.rk', '.alz', '.bzip2', '.rnc', '.s01', '.rss', '.vpk', '.mzp', '.nz', '.spt', '.tgz', '.jex', '.pup', '.car', '.arj', '.tar.lzma', '.stkdoodlz', '.paq8p', '.fp8', '.mlproj', '.xar', '.xmcdz', '.bzip', '.lzh', '.jhh', '.zfsendtotarget', '.z04', '.jgz', '.000', '.zoo', '.zsplit', '.rp9', '.lbr', '.tar.bz2', '.shr', '.pet', '.xez', '.j', '.tcx', '.lha', '.sar', '.iadproj', '.z00', '.zi_', '.ish', '.snappy', '.sea', '.srep', '.hyp', '.pax', '.zi', '.mzp', '.ain', '.hki3', '.zap', '.comppkg_hauptwerk_rar', '.r04', '.psz', '.lhzd', '.hki1', '.libzip', '.spl', '.z01', '.shk', '.dgc', '.mbz', '.gz2', '.cpt', '.pima', '.ecsbx', '.paq8f', '.gzi', '.vib', '.lzr', '.z02', '.isx', '.edz', '.nar', '.pbi', '.xoj', '.bza', '.b64', '.lqr', '.vmcz', '.ize', '.wdz', '.tz', '.hbc', '.zz', '.egg', '.ipg', '.wux', '.txz', '.md', '.layout', '.zw', '.cpgz', '.pvmp', '.wacz', '.pack.gz', '.hpkg', '.pkg.tar.zst', '.tg', '.tar.z', '.spm', '.vsi', '.hpk', '.prs', '.hbc2', '.tlz', '.c02', '.xzm', '.uc2', '.yc', '.lzo', '.movpkg', '.mou', '.puz', '.waff', '.uzed', '.uzip', '.arh', '.mar', '.snz', '.pae', '.jic', '.snagitstamps', '.yz1', '.daf', '.zim', '.stg', '.mozlz4', '.paq6', '.vwi', '.zabw', '.kz', '.ha', '.r02', '.pim', '.bdoc', '.wot', '.gar', '.trs', '.lzx', '.dist', '.sdn', '.pvmz', '.r21', '.ana', '.paq8l', '.asice', '.conda', '.y', '.sen', '.efw', '.tlzma', '.r1', '.pxl', '.p01', '.paq7', '.wlb', '.stproj', '.sipa', '.kwgt', '.cp9', '.odlgz', '.s09', '.hki2', '.vms', '.fcx', '.sqf', '.boo', '.tar.gz2', '.sbx', '.ufdr', '.bzabw', '.zed', '.vfs', '.vem', '.paq8', '.sbx', '.sqz', '.xfp'],
    "eBook": ['.tpz', '.mart', '.apnx', '.ea', '.lrf', '.tk3', '.jwpub', '.ibooks', '.mobi', '.aep', '.tr', '.ncx', '.dnl', '.azw3', '.fb2', '.rzs', '.lrs', '.ybk', '.opf', '.lit', '.rzb', '.azw4', '.ceb', '.han', '.epub', '.nva', '.htz5', '.ebk', '.opf', '.prc', '.webz', '.mbp', '.cbc', '.lrx', '.kfx', '.azw', '.phl', '.acsm', '.tcr', '.ava', '.oeb', '.edn', '.orb', '.htz4', '.htxt', '.opz', '.tr3', '.cebx', '.snb', '.etd', '.html0', '.eal', '.azw1', '.pobi', '.htmlz', '.koob', '.qmk', '.vbk', '.bpnueb', '.pef', '.oebzip', '.fkb', '.pmlz', '.bkk', '.pml'],
    "Other": []
}

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

selected_days = []

checked_items = {}

final_checked_items = {}

categorized_files = {}
tester = {}
excluded_files = {}

exclusion_status = {}



checkboxes = {}

selected_folder_paths_manual = []

selected_folder_paths_automated = []

day_checkboxes_dict = {}

is_toggled = False

is_automated = None

included_tree = None

excluded_tree = None

# MAIN FUNCTIONS
#-----------------------------------------------------------------------------------------------------------------------

# try to use these more??????????????
def get_excluded_tree(tree):
    global excluded_tree
    excluded_tree = tree


def get_inlcuded_tree(tree):
    global included_tree
    included_tree = tree

def merge_items_together(folder_list, items_tree):
    global categorized_files, excluded_files

    selected_folders = folder_list.selectedItems()


    selected_item = items_tree.selectedItems()[0]

    depth = get_item_depth(selected_item)

    for folder in selected_folders:
        selected_folder_name = folder.text()

        # Initialize a reference to the current level of the nested dictionary
        current_level = excluded_files

        if depth == 0:
            folder_path = selected_folder_name
            category = selected_item.text(0)


            if folder_path not in current_level:
                current_level[folder_path] = {}

            if category not in current_level[folder_path]:
                current_level[folder_path][category] = {}

            for i in range(selected_item.childCount()):
                child_item = selected_item.child(i)
                file_type = child_item.text(0)

                if file_type not in current_level[folder_path][category]:
                    current_level[folder_path][category][file_type] = []


        elif depth == 1:
            folder_path = selected_folder_name
            category = selected_item.parent().text(0)
            file_type = selected_item.text(0)

            if folder_path not in current_level:
                current_level[folder_path] = {}
            if category not in current_level[folder_path]:
                current_level[folder_path][category] = {}
            if file_type not in current_level[folder_path][category]:
                current_level[folder_path][category][file_type] = []





    idk_name_yet(included_tree, excluded_tree)

    print(excluded_files)






def open_and_select_folder(listWidget, treeWidget, excluded_tree):
    # Create options for the file dialog
    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly  # Add the ReadOnly option

    # Open the folder dialog and get the selected folder path
    folder_path = QFileDialog.getExistingDirectory(None, "Select a folder", options=options)

    if is_automated:
        selected_folders = selected_folder_paths_automated
    else:
        selected_folders = selected_folder_paths_manual

    if folder_path:
        if folder_path in selected_folders:
            # Display a warning message if the folder path is already selected
            QMessageBox.warning(None, "Folder Already Selected", "This folder has already been selected.")
        else:
            # Check if there are any files (not directories) in the selected folder.
            files_with_extensions = any(os.path.isfile(os.path.join(folder_path, filename)) for filename in os.listdir(folder_path))
            if not files_with_extensions:
                # Display a warning message if there are no files with extensions
                QMessageBox.warning(None, "No Files with Extensions", "There are no files in this folder.")
            else:
                # Add the folder path to the list
                if is_automated:
                    selected_folder_paths_automated.append(folder_path)

                    # Update and add the selected folder to the list widget
                    update_list_widget(listWidget, selected_folder_paths_automated)

                    idk_name_yet(treeWidget, excluded_tree)

                else:
                    selected_folder_paths_manual.append(folder_path)

                    # Update and add the selected folder to the list widget
                    update_list_widget(listWidget, selected_folder_paths_manual)

                    # Categorize the files
                    categorize_files(treeWidget, selected_folder_paths_manual)

def update_list_widget(listWidget,selected_folder_paths):
    # Clear the existing items in the list widget
    listWidget.clear()
    # Add the selected folder paths to the list widget
    listWidget.addItems(selected_folder_paths)

def categorize_files(treeWidget,selected_folder_paths):

    # Loop through each selected folder path
    for source_folder in selected_folder_paths:
        # Loop through files in the source folder
        for filename in os.listdir(source_folder):
            file_extension = os.path.splitext(filename)[1]
            if file_extension:
                # Look for the file extension in the dictionary file_categories
                for category, extensions in file_categories.items():
                    if file_extension in extensions:
                        if source_folder not in categorized_files:
                            # Create an entry for the source folder in the categorized files dictionary
                            # with an empty dictionary as its value
                            categorized_files[source_folder] = {}
                        if category not in categorized_files[source_folder]:
                            # Create an entry for the category within the source folder in the categorized files dictionary
                            # with an empty dictionary as its value
                            categorized_files[source_folder][category] = {}
                        if file_extension not in categorized_files[source_folder][category]:
                            # Create an empty list with the file extension as the key
                            categorized_files[source_folder][category][file_extension] = []
                        # Add the file to the file extension list
                        categorized_files[source_folder][category][file_extension].append(filename)



    treeWidget.clear()

        # Populate the tree widget with the categorized files and folders stored in the categorized_files dictionary
    populate_tree(treeWidget, categorized_files)



def populate_tree(treeWidget, categorized_files_dictionary, is_browse_window=None, item=None):
    # Loop through keys and values in the categorized_files_dictionary
    for category_or_extension_name, values in categorized_files_dictionary.items():
        # If there's no parent item (top-level item):
        if item is None:
            # Create a new top-level item in the tree_view
            tree_view_item = QtWidgets.QTreeWidgetItem(treeWidget)
            # Set the text of the item to the current key
            tree_view_item.setText(0, category_or_extension_name)
        else:
            # Create a new child item under the parent item
            tree_view_item = QtWidgets.QTreeWidgetItem(item)
            # Set the text of the item to the current key
            tree_view_item.setText(0, category_or_extension_name)

        if not is_automated:
            # Only add checkboxes if is_automated is False
            tree_view_item.setFlags(tree_view_item.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            tree_view_item.setCheckState(0, Qt.Unchecked)

        if isinstance(values, dict):
            # When it encounters a dictionary as a value, there are nested items or subcategories to be added.
            populate_tree(treeWidget, values, None, tree_view_item)

        elif isinstance(values, list):
            if is_browse_window or not is_automated:

                # Loop through each filename in the list
                for filename in values:
                    # Create a new child item under the current item
                    child = QtWidgets.QTreeWidgetItem(tree_view_item)
                    # Set the text of the child item to the filename
                    child.setText(0, filename)

                    if not is_automated:
                        # Add special attributes for user interaction to the child item
                        child.setFlags(child.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsTristate)
                        # Set the initial check state of the child item to unchecked
                        child.setCheckState(0, Qt.Unchecked)

    # After populating the tree with categorized_files, sort the items alphabetically
    treeWidget.sortItems(0, Qt.AscendingOrder)



def getting_checked_items(treeWidget):
    global categorized_files, checked_items, tester

    categorize_checked_items(treeWidget)

    categorize_files(treeWidget, selected_folder_paths_automated)

    delete_items_from_dict(categorized_files, checked_items)

    tester = categorized_files

def organize_chosen_files(treeWidget, remove_duplicates_checkbox, selected_folder_paths, excluded_tree):
    global categorized_files, checked_items

    def calculate_file_hash(file_path, hash_function=hashlib.md5, buffer_size=65536):
        hash_obj = hash_function()
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(buffer_size)
                if not data:
                    break
                hash_obj.update(data)
        return hash_obj.hexdigest()

    def find_and_delete_duplicate_files(directory):
        # Create a dictionary to store file hashes and their paths
        file_hashes = {}

        for root, dirs, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_hash = calculate_file_hash(file_path)

                if file_hash in file_hashes:
                    # We found a duplicate file
                    print(f'Duplicate file found: {file_path} and {file_hashes[file_hash]}')
                    # Delete the duplicate file
                    os.remove(file_path)
                    print(f'Deleted duplicate file: {file_path}')
                else:
                    # Add the file hash to the dictionary
                    file_hashes[file_hash] = file_path

    for folder_path, folders in categorized_files.items():
        print(folder_path)
        for category, categories in folders.items():
            print(category)
            for file_type, file_types in categories.items():
                print(file_type)
                for file in file_types:
                    print(file)



                    new_folder_path = os.path.join(folder_path, category, file_type[1:])
                    os.makedirs(new_folder_path, exist_ok=True)

                    source_file = os.path.join(folder_path, file)
                    destination_file = os.path.join(new_folder_path, file)

                    # if the file doesnt exist in the directiory
                    if remove_duplicates_checkbox.isChecked():
                        print("Checking for duplicates and removing them...")
                        find_and_delete_duplicate_files(new_folder_path)

                    try:
                        shutil.move(source_file, destination_file)
                        print(f"Moved '{file}' to '{destination_file}'")
                    except Exception as e:
                        print(f"Error moving '{file}' to '{destination_file}': {e}")



    # After organizing files, refresh the QTreeWidget and re-categorize the files
    treeWidget.clear()  # Clear the existing items in the QTreeWidget
    categorized_files = {}  # Clear the categorized_files dictionary
    idk_name_yet(treeWidget,excluded_tree)


# MANUAL FUNCTIONS
#-----------------------------------------------------------------------------------------------------------------------

def get_item_depth(tree_item):
    depth = 0
    parent = tree_item.parent()
    while parent is not None:
        depth += 1
        parent = parent.parent()
    return depth


from PyQt5 import QtCore


def check_saved_items(treeWidget):
    global checked_items

    # Iterate through the treeWidget items and check those not in checked_items
    for tree_item in treeWidget.findItems("", QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive):
        tree_item.setCheckState(0, QtCore.Qt.Unchecked)

    # Iterate through checked_items and set check state to Checked
    for folder_path, folders in tester.items():
        for category, categories in folders.items():



            for file_type, file_types in categories.items():

                file_type_items = treeWidget.findItems(file_type, QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive)

                # Check the lower-level tree view items (depth 2)
                for item in file_type_items:
                    itemlol = item.text(0)
                    file_type_item = item
                    category_item = file_type_item.parent()
                    folder_item = category_item.parent()

                    # Get the name of the top-level item from the first column
                    top_level_name = folder_item.text(0)

                    if top_level_name == folder_path:
                        item.setCheckState(0, QtCore.Qt.Checked)  # Set the check state to Checked

                        # Check the children of the item
                        for child_index in range(item.childCount()):
                            if child_index == 0:
                                break
                            else:
                                child_item = item.child(child_index)
                                child_item.setCheckState(0, QtCore.Qt.Checked)




                for file in file_types:
                    # Find the item in the tree widget
                    file_items = treeWidget.findItems(file, QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive)

                    # Check the lower-level tree view items (depth 3)
                    for item in file_items:
                        itemlol = item.text(0)
                        file_type_item = item.parent()
                        category_item = file_type_item.parent()
                        folder_item = category_item.parent()

                        # Get the name of the top-level item from the first column
                        top_level_name = folder_item.text(0)

                        if top_level_name == folder_path:
                            item.setCheckState(0, QtCore.Qt.Checked)  # Set the check state to Checked


# AUTOMATED FUNCTIONS
#-----------------------------------------------------------------------------------------------------------------------
def exclude_files(included_tree,excluded_tree):
    global categorized_files, excluded_files
    excluded_tree.clear()

    selected_item = included_tree.selectedItems()[0]

    depth = get_item_depth(selected_item)

    # Initialize a reference to the current level of the nested dictionary
    current_level = excluded_files

    if depth == 0:
        folder_path = selected_item.text(0)

        if folder_path not in current_level:
            current_level[folder_path] = {}

        for i in range(selected_item.childCount()):
            child_item = selected_item.child(i)
            category = child_item.text(0)

            if category not in current_level[folder_path]:
                current_level[folder_path][category] = {}

            for j in range(child_item.childCount()):  # Use a different variable here
                grand_child_item = child_item.child(j)
                file_type = grand_child_item.text(0)

                if file_type not in current_level[folder_path][category]:
                    current_level[folder_path][category][file_type] = []


    elif depth == 1:
        folder_path = selected_item.parent().text(0)
        category = selected_item.text(0)


        if folder_path not in current_level:
            current_level[folder_path] = {}

        if category not in current_level[folder_path]:
            current_level[folder_path][category] = {}

        for i in range(selected_item.childCount()):
            child_item = selected_item.child(i)
            file_type = child_item.text(0)

            if file_type not in current_level[folder_path][category]:
                current_level[folder_path][category][file_type] = []


    elif depth == 2:
        folder_path = selected_item.parent().parent().text(0)
        category = selected_item.parent().text(0)
        file_type = selected_item.text(0)

        if folder_path not in current_level:
            current_level[folder_path] = {}
        if category not in current_level[folder_path]:
            current_level[folder_path][category] = {}
        if file_type not in current_level[folder_path][category]:
            current_level[folder_path][category][file_type] = []



    print(excluded_files)
    idk_name_yet(included_tree, excluded_tree)


def include_files(included_tree, excluded_tree):
    global categorized_files, excluded_files

    selected_item = excluded_tree.selectedItems()[0]
    depth = get_item_depth(selected_item)

    # Initialize a reference to the current level of the nested dictionary
    current_level = excluded_files

    if depth == 0:
        folder_path = selected_item.text(0)

        if folder_path in current_level:
            current_level.pop(folder_path)

    elif depth == 1:
        folder_path = selected_item.parent().text(0)
        category = selected_item.text(0)

        if folder_path in current_level and category in current_level[folder_path]:
            current_level[folder_path].pop(category)

            # Check if the folder is empty, and if so, remove it
            if not current_level[folder_path]:
                current_level.pop(folder_path)

    elif depth == 2:
        folder_path = selected_item.parent().parent().text(0)
        category = selected_item.parent().text(0)
        file_type = selected_item.text(0)

        if folder_path in current_level and category in current_level[folder_path] and file_type in \
                current_level[folder_path][category]:
            current_level[folder_path][category].pop(file_type)

            # Check if the category is empty, and if so, remove it
            if not current_level[folder_path][category]:
                current_level[folder_path].pop(category)

            # Check if the folder is empty, and if so, remove it
            if not current_level[folder_path]:
                current_level.pop(folder_path)

    print(excluded_files)
    excluded_tree.clear()
    idk_name_yet(included_tree, excluded_tree)


def idk_name_yet(included_tree, excluded_tree):
    global excluded_files, categorized_files

    excluded_tree.clear()
    populate_tree(excluded_tree, excluded_files)

    categorize_files(included_tree, selected_folder_paths_automated)

    if len(categorized_files) != 0:
        delete_items_from_dict(categorized_files, excluded_files)

    included_tree.clear()
    populate_tree(included_tree, categorized_files)

    print(categorized_files)

def delete_items_from_dict(target_dict, items_to_delete):


            for key, value in items_to_delete.items():


                    if isinstance(value, dict):
                        # Recursively call the function to process nested dictionaries
                        if key in target_dict:
                            delete_items_from_dict(target_dict[key], value)
                        else:
                            print("lol")
                            continue
                        # Check if the category is empty after processing
                        if not target_dict[key]:
                            del target_dict[key]
                    elif key in target_dict:
                        # If the key exists in the target_dict, delete it
                        del target_dict[key]





def categorize_checked_items(treeWidget):
        global checked_items
        # Clear the existing nested dictionary
        checked_items = {}

        # Iterate through all items in the tree widget
        for tree_item in treeWidget.findItems("", QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive):
            # Check if the item is checked or partially checked
            if tree_item.checkState(0) == QtCore.Qt.Unchecked:

                depth = get_item_depth(tree_item)

                # Initialize a reference to the current level of the nested dictionary
                current_level = checked_items

                if depth == 0:
                    folder_path = tree_item.text(0)

                    if folder_path not in current_level:
                        current_level[folder_path] = {}

                elif depth == 1:
                    folder_path = tree_item.parent().text(0)
                    category = tree_item.text(0)

                    if folder_path not in current_level:
                        current_level[folder_path] = {}
                    if category not in current_level[folder_path]:
                        current_level[folder_path][category] = {}

                elif depth == 2:
                    folder_path = tree_item.parent().parent().text(0)
                    category = tree_item.parent().text(0)
                    file_type = tree_item.text(0)

                    if folder_path not in current_level:
                        current_level[folder_path] = {}
                    if category not in current_level[folder_path]:
                        current_level[folder_path][category] = {}
                    if file_type not in current_level[folder_path][category]:
                        current_level[folder_path][category][file_type] = []

                else:
                    continue
        print("lol")



# EXTRA FUNCTIONS
#-----------------------------------------------------------------------------------------------------------------------

def toggle_select_all(list_widget):
    list_widget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
    for index in range(list_widget.count()):
        item = list_widget.item(index)
        item.setSelected(True)
    list_widget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)


def delete_selected_folder(listWidget, treeWidget, excluded_tree):
    global selected_folder_paths_automated, selected_folder_paths_manual
    selected_items = listWidget.selectedItems()

    if is_automated:
        selected_folder_paths = selected_folder_paths_automated
    else:
        selected_folder_paths = selected_folder_paths_manual

    if selected_items:
        selected_item = selected_items[0].text()

        if selected_item in selected_folder_paths:
            selected_folder_paths.remove(selected_item)  # Remove the selected folder path
            print("Deleted folder:", selected_item)

            # Update the QListWidget with the modified folder paths
            listWidget.clear()  # Clear the existing items
            listWidget.addItems(selected_folder_paths)  # Add the modified folder paths

            # Delete the folder from the categorized_files dictionary
            for source_folder in list(categorized_files.keys()):
                if source_folder == selected_item:
                    del categorized_files[source_folder]

    idk_name_yet(treeWidget,excluded_tree)

# JSON MANUAL
#-----------------------------------------------------------------------------------------------------------------------



# JSON AUTOMATED
#-----------------------------------------------------------------------------------------------------------------------
# Function to save the state of the "Remove Duplicates" checkbox
def save_remove_duplicates_state(state):
    with open('remove_duplicates_state.pickle', 'wb') as file:
        pickle.dump(state, file)

# Function to load the state of the "Remove Duplicates" checkbox
def load_remove_duplicates_state():
    try:
        with open('remove_duplicates_state.pickle', 'rb') as file:
            state = pickle.load(file)
            return state
    except FileNotFoundError:
        return False  # Default to False if the file doesn't exist or hasn't been saved yet



# Function to save the dictionary to a file
def save_excluded_files():
    global excluded_files
    with open("excluded_files.json", 'w') as file:
        json.dump(excluded_files, file)

# Function to load the dictionary from a file
def load_excluded_files(included_tree, excluded_tree):
    global excluded_files
    try:
        with open("excluded_files.json", 'r') as file:
            excluded_files = json.load(file)
            idk_name_yet(included_tree, excluded_tree)

    except FileNotFoundError:
        print("no file found")


def save_selected_folders():

    if is_automated:
        folders = selected_folder_paths_automated
        json_string = "selected_folders_automated.json"
    else:
        folders = selected_folder_paths_manual
        json_string = "selected_folders_manual.json"


    # Save the list of selected folder paths to a JSON file
    with open(json_string, "w") as json_file:
        json.dump(folders, json_file)

def load_selected_folders(listWidget):


    if is_automated:
        json_string = "selected_folders_automated.json"
    else:
        json_string = "selected_folders_manual.json"



    if os.path.exists(json_string):
        with open(json_string, "r") as json_file:
            global selected_folder_paths_manual, selected_folder_paths_automated
            folders = json.load(json_file)
            if is_automated:
                selected_folder_paths_automated = folders
            else:
                selected_folder_paths_manual = folders

            update_list_widget(listWidget, folders)  # Update the list widget with the loaded folder paths


def load_checked_items(treeWidget):
    if is_automated:
        global tester
        # Check if the JSON file with checked item state exists

        if os.path.exists("checked_items.json"):
            with open("checked_items.json", "r") as json_file:
                tester = json.load(json_file)
                check_saved_items(treeWidget)

def save_checked_items():
    if is_automated:
        global tester
        with open("checked_items.json", "w") as json_file:
            json.dump(tester, json_file)


checkbox_states = {}
def save_selected_days():
    # Save the checkbox states to a JSON file
    with open('checkbox_states.json', 'w') as f:
        json.dump({day: checkbox.isChecked() for day, checkbox in day_checkboxes_dict.items()}, f)

def load_selected_days():
    # Load the checkbox states from a JSON file, if it exists
    try:
        with open('checkbox_states.json', 'r') as f:
            data = json.load(f)
            for day, checked in data.items():
                if checked:
                    day_checkboxes_dict[day].setChecked(checked)

    except FileNotFoundError:
        pass

def save_toggle_state():

    config_data = {"is_toggled": is_toggled}
    with open("toggle_state.json", "w") as file:
        json.dump(config_data, file)

def load_toggle_state():
    global is_toggled
    # Check if the configuration file exists
    if os.path.isfile("toggle_state.json"):
        with open("toggle_state.json", "r") as file:
            config_data = json.load(file)
            is_toggled = config_data.get("is_toggled")
    else:
        is_toggled = False



# TREE SELECTION
#-----------------------------------------------------------------------------------------------------------------------

def select_item_in_tree(file_overview_tree):
    selected_items = file_overview_tree.selectedItems()
    current_level = checked_items

    for item in selected_items:
        print(item.text(0))

    for tree_item in selected_items:
        depth = get_item_depth(tree_item)

        if depth == 0:
            folder_path = tree_item.text(0)
            current_level[folder_path] = {}
        elif depth == 1:
            category = tree_item.text(0)
            current_level[folder_path][category] = {}
        elif depth == 2:
            file_type = tree_item.text(0)
            current_level[folder_path][category][file_type] = []
        elif depth == 3:
            file = tree_item.text(0)
            current_level[folder_path][category][file_type].append(file)

def find_top_level_parent(item):
    parent = item.parent()
    while parent is not None:
        item = parent
        parent = item.parent()
    return item

def get_selected_item(treeWidget):
    selected_items = treeWidget.selectedItems()
    if selected_items:
        print(selected_items[0].text)
        top_level_parent = find_top_level_parent(selected_items[0])
        return top_level_parent  # Assuming you want the first selected item
    else:
        return None


# DAYS
#-----------------------------------------------------------------------------------------------------------------------

def check_current_day(selected_days, duplicates_checkbox, tree_widget, excluded_tree):
    # Get the current day (e.g., "Mon", "Tue")
    current_day = QtCore.QDate.currentDate().toString("ddd")
    print(current_day)

    # Check if the current day is in the selected days
    if current_day in selected_days:
        print("yes today needs to be organized")

        if len(categorized_files) != 0:
            organize_chosen_files(tree_widget,duplicates_checkbox, selected_folder_paths_automated, excluded_tree)


    else:
        print("nothing needs to be organized today")


