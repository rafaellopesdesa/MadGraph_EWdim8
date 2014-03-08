# This file was automatically created by FeynRules 2.0.17
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (November 20, 2012)
# Date: Fri 21 Feb 2014 15:19:32


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.G, P.G, P.G ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_12})

V_2 = Vertex(name = 'V_2',
             particles = [ P.G, P.G, P.G, P.G ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV2, L.VVVV6, L.VVVV7 ],
             couplings = {(1,1):C.GC_14,(0,0):C.GC_14,(2,2):C.GC_14})

V_3 = Vertex(name = 'V_3',
             particles = [ P.A, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_65})

V_4 = Vertex(name = 'V_4',
             particles = [ P.A, P.A, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVVV3, L.VVVV5, L.VVVV9 ],
             couplings = {(0,0):C.GC_145,(0,1):C.GC_79,(0,2):C.GC_144})

V_5 = Vertex(name = 'V_5',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_15})

V_6 = Vertex(name = 'V_6',
             particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVVV14, L.VVVV4, L.VVVV5 ],
             couplings = {(0,0):C.GC_154,(0,1):C.GC_152,(0,2):C.GC_21})

V_7 = Vertex(name = 'V_7',
             particles = [ P.A, P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVVV1, L.VVVV11, L.VVVV12, L.VVVV8 ],
             couplings = {(0,2):C.GC_162,(0,1):C.GC_168,(0,0):C.GC_161,(0,3):C.GC_70})

V_8 = Vertex(name = 'V_8',
             particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVVV15, L.VVVV16, L.VVVV18, L.VVVV3, L.VVVV5, L.VVVV9 ],
             couplings = {(0,1):C.GC_146,(0,0):C.GC_155,(0,3):C.GC_171,(0,2):C.GC_153,(0,4):C.GC_22,(0,5):C.GC_196})

V_9 = Vertex(name = 'V_9',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_30})

V_10 = Vertex(name = 'V_10',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_113})

V_11 = Vertex(name = 'V_11',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_32,(0,1):C.GC_7,(0,2):C.GC_4})

V_12 = Vertex(name = 'V_12',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_114})

V_13 = Vertex(name = 'V_13',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_85,(0,1):C.GC_8,(0,2):C.GC_5})

V_14 = Vertex(name = 'V_14',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_176})

V_15 = Vertex(name = 'V_15',
              particles = [ P.d__tilde__, P.d, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_13})

V_16 = Vertex(name = 'V_16',
              particles = [ P.s__tilde__, P.s, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_13})

V_17 = Vertex(name = 'V_17',
              particles = [ P.b__tilde__, P.b, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_13})

V_18 = Vertex(name = 'V_18',
              particles = [ P.u__tilde__, P.u, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_13})

V_19 = Vertex(name = 'V_19',
              particles = [ P.c__tilde__, P.c, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_13})

V_20 = Vertex(name = 'V_20',
              particles = [ P.t__tilde__, P.t, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_13})

V_21 = Vertex(name = 'V_21',
              particles = [ P.d__tilde__, P.d, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_22 = Vertex(name = 'V_22',
              particles = [ P.s__tilde__, P.s, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_23 = Vertex(name = 'V_23',
              particles = [ P.b__tilde__, P.b, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_24 = Vertex(name = 'V_24',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_47,(0,1):C.GC_59})

V_25 = Vertex(name = 'V_25',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_47,(0,1):C.GC_59})

V_26 = Vertex(name = 'V_26',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,1):C.GC_59,(0,0):C.GC_47})

V_27 = Vertex(name = 'V_27',
              particles = [ P.e__plus__, P.e__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_28 = Vertex(name = 'V_28',
              particles = [ P.m__plus__, P.m__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_29 = Vertex(name = 'V_29',
              particles = [ P.tt__plus__, P.tt__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_30 = Vertex(name = 'V_30',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_47,(0,1):C.GC_60})

V_31 = Vertex(name = 'V_31',
              particles = [ P.m__plus__, P.m__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_47,(0,1):C.GC_60})

V_32 = Vertex(name = 'V_32',
              particles = [ P.tt__plus__, P.tt__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_47,(0,1):C.GC_60})

V_33 = Vertex(name = 'V_33',
              particles = [ P.u__tilde__, P.u, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_34 = Vertex(name = 'V_34',
              particles = [ P.c__tilde__, P.c, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_35 = Vertex(name = 'V_35',
              particles = [ P.t__tilde__, P.t, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_36 = Vertex(name = 'V_36',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,1):C.GC_59,(0,0):C.GC_48})

V_37 = Vertex(name = 'V_37',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_48,(0,1):C.GC_59})

V_38 = Vertex(name = 'V_38',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_48,(0,1):C.GC_59})

V_39 = Vertex(name = 'V_39',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_84})

V_40 = Vertex(name = 'V_40',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_84})

V_41 = Vertex(name = 'V_41',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_84})

V_42 = Vertex(name = 'V_42',
              particles = [ P.e__plus__, P.ve, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_42})

V_43 = Vertex(name = 'V_43',
              particles = [ P.m__plus__, P.vm, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_42})

V_44 = Vertex(name = 'V_44',
              particles = [ P.tt__plus__, P.vt, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_42})

V_45 = Vertex(name = 'V_45',
              particles = [ P.d__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_43})

V_46 = Vertex(name = 'V_46',
              particles = [ P.s__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_44})

V_47 = Vertex(name = 'V_47',
              particles = [ P.d__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_45})

V_48 = Vertex(name = 'V_48',
              particles = [ P.s__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_46})

V_49 = Vertex(name = 'V_49',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_42})

V_50 = Vertex(name = 'V_50',
              particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_42})

V_51 = Vertex(name = 'V_51',
              particles = [ P.vm__tilde__, P.m__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_42})

V_52 = Vertex(name = 'V_52',
              particles = [ P.vt__tilde__, P.tt__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_42})

V_53 = Vertex(name = 'V_53',
              particles = [ P.u__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_213})

V_54 = Vertex(name = 'V_54',
              particles = [ P.c__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_215})

V_55 = Vertex(name = 'V_55',
              particles = [ P.u__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_214})

V_56 = Vertex(name = 'V_56',
              particles = [ P.c__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_216})

V_57 = Vertex(name = 'V_57',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_42})

V_58 = Vertex(name = 'V_58',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_210})

V_59 = Vertex(name = 'V_59',
              particles = [ P.tt__plus__, P.tt__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_212})

V_60 = Vertex(name = 'V_60',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_211})

V_61 = Vertex(name = 'V_61',
              particles = [ P.A, P.A, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_75,(0,1):C.GC_74})

V_62 = Vertex(name = 'V_62',
              particles = [ P.A, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_62,(0,1):C.GC_61})

V_63 = Vertex(name = 'V_63',
              particles = [ P.A, P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSS2, L.VVVSS4, L.VVVSS5 ],
              couplings = {(0,0):C.GC_9,(0,1):C.GC_67,(0,2):C.GC_66})

V_64 = Vertex(name = 'V_64',
              particles = [ P.A, P.A, P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS17, L.VVVVSS2, L.VVVVSS21, L.VVVVSS4, L.VVVVSS6 ],
              couplings = {(0,1):C.GC_10,(0,0):C.GC_68,(0,3):C.GC_81,(0,4):C.GC_6,(0,2):C.GC_80})

V_65 = Vertex(name = 'V_65',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSS1, L.VVVSS3, L.VVVSS4, L.VVVSS5 ],
              couplings = {(0,1):C.GC_50,(0,0):C.GC_63,(0,2):C.GC_17,(0,3):C.GC_16})

V_66 = Vertex(name = 'V_66',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS11, L.VVVVSS19, L.VVVVSS21, L.VVVVSS3, L.VVVVSS4 ],
              couplings = {(0,0):C.GC_35,(0,1):C.GC_53,(0,4):C.GC_26,(0,3):C.GC_33,(0,2):C.GC_23})

V_67 = Vertex(name = 'V_67',
              particles = [ P.A, P.A, P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVS15, L.VVVVS2, L.VVVVS4 ],
              couplings = {(0,1):C.GC_105,(0,0):C.GC_136,(0,2):C.GC_103})

V_68 = Vertex(name = 'V_68',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVS17, L.VVVVS3, L.VVVVS9 ],
              couplings = {(0,2):C.GC_117,(0,0):C.GC_128,(0,1):C.GC_115})

V_69 = Vertex(name = 'V_69',
              particles = [ P.A, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS1, L.VVVVSS18, L.VVVVSS20, L.VVVVSS22, L.VVVVSS5, L.VVVVSS8, L.VVVVSS9 ],
              couplings = {(0,6):C.GC_51,(0,5):C.GC_64,(0,2):C.GC_18,(0,1):C.GC_77,(0,4):C.GC_72,(0,0):C.GC_49,(0,3):C.GC_71})

V_70 = Vertex(name = 'V_70',
              particles = [ P.A, P.W__minus__, P.W__plus__, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVS1, L.VVVVS16, L.VVVVS18, L.VVVVS6, L.VVVVS7 ],
              couplings = {(0,4):C.GC_126,(0,3):C.GC_135,(0,2):C.GC_107,(0,1):C.GC_140,(0,0):C.GC_124})

V_71 = Vertex(name = 'V_71',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS12, L.VVVVSS13, L.VVVVSS15, L.VVVVSS17, L.VVVVSS19, L.VVVVSS2, L.VVVVSS21, L.VVVVSS4, L.VVVVSS6 ],
              couplings = {(0,1):C.GC_11,(0,0):C.GC_36,(0,5):C.GC_76,(0,2):C.GC_34,(0,4):C.GC_54,(0,3):C.GC_68,(0,7):C.GC_27,(0,8):C.GC_87,(0,6):C.GC_24})

V_72 = Vertex(name = 'V_72',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVS10, L.VVVVS11, L.VVVVS13, L.VVVVS15, L.VVVVS17, L.VVVVS2, L.VVVVS4 ],
              couplings = {(0,1):C.GC_106,(0,0):C.GC_118,(0,5):C.GC_139,(0,2):C.GC_116,(0,4):C.GC_129,(0,3):C.GC_136,(0,6):C.GC_178})

V_73 = Vertex(name = 'V_73',
              particles = [ P.A, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVVSS15, L.VVVVVSS2 ],
              couplings = {(0,0):C.GC_55,(0,1):C.GC_52})

V_74 = Vertex(name = 'V_74',
              particles = [ P.A, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVVS15, L.VVVVVS2 ],
              couplings = {(0,0):C.GC_130,(0,1):C.GC_127})

V_75 = Vertex(name = 'V_75',
              particles = [ P.A, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVV14, L.VVVVV2 ],
              couplings = {(0,0):C.GC_164,(0,1):C.GC_163})

V_76 = Vertex(name = 'V_76',
              particles = [ P.A, P.A, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVVVSS1, L.VVVVVVSS5 ],
              couplings = {(0,1):C.GC_28,(0,0):C.GC_25})

V_77 = Vertex(name = 'V_77',
              particles = [ P.A, P.A, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVVVS1, L.VVVVVVS5 ],
              couplings = {(0,1):C.GC_111,(0,0):C.GC_110})

V_78 = Vertex(name = 'V_78',
              particles = [ P.A, P.A, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV1, L.VVVVVV5 ],
              couplings = {(0,1):C.GC_150,(0,0):C.GC_149})

V_79 = Vertex(name = 'V_79',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVVSS10, L.VVVVVSS14, L.VVVVVSS9 ],
              couplings = {(0,2):C.GC_19,(0,0):C.GC_37,(0,1):C.GC_38})

V_80 = Vertex(name = 'V_80',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVVS10, L.VVVVVS14, L.VVVVVS9 ],
              couplings = {(0,2):C.GC_108,(0,0):C.GC_119,(0,1):C.GC_120})

V_81 = Vertex(name = 'V_81',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV13, L.VVVVV8, L.VVVVV9 ],
              couplings = {(0,1):C.GC_147,(0,2):C.GC_156,(0,0):C.GC_157})

V_82 = Vertex(name = 'V_82',
              particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVVVSS9 ],
              couplings = {(0,0):C.GC_31})

V_83 = Vertex(name = 'V_83',
              particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVVVS9 ],
              couplings = {(0,0):C.GC_175})

V_84 = Vertex(name = 'V_84',
              particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV9 ],
              couplings = {(0,0):C.GC_194})

V_85 = Vertex(name = 'V_85',
              particles = [ P.A, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVVVSS11, L.VVVVVVSS12, L.VVVVVVSS8 ],
              couplings = {(0,1):C.GC_57,(0,2):C.GC_58,(0,0):C.GC_73})

V_86 = Vertex(name = 'V_86',
              particles = [ P.A, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVVVS11, L.VVVVVVS12, L.VVVVVVS8 ],
              couplings = {(0,1):C.GC_132,(0,2):C.GC_133,(0,0):C.GC_138})

V_87 = Vertex(name = 'V_87',
              particles = [ P.A, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV11, L.VVVVVV12, L.VVVVVV8 ],
              couplings = {(0,1):C.GC_166,(0,2):C.GC_167,(0,0):C.GC_170})

V_88 = Vertex(name = 'V_88',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVVVSS13, L.VVVVVVSS2, L.VVVVVVSS4, L.VVVVVVSS6, L.VVVVVVSS7 ],
              couplings = {(0,4):C.GC_29,(0,3):C.GC_41,(0,1):C.GC_82,(0,0):C.GC_40,(0,2):C.GC_91})

V_89 = Vertex(name = 'V_89',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVVVS13, L.VVVVVVS2, L.VVVVVVS4, L.VVVVVVS6, L.VVVVVVS7 ],
              couplings = {(0,4):C.GC_112,(0,3):C.GC_123,(0,1):C.GC_142,(0,0):C.GC_122,(0,2):C.GC_182})

V_90 = Vertex(name = 'V_90',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV13, L.VVVVVV2, L.VVVVVV4, L.VVVVVV6, L.VVVVVV7 ],
              couplings = {(0,4):C.GC_151,(0,3):C.GC_160,(0,1):C.GC_173,(0,0):C.GC_159,(0,2):C.GC_200})

V_91 = Vertex(name = 'V_91',
              particles = [ P.A, P.A, P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS2, L.VVVVSS6 ],
              couplings = {(0,0):C.GC_100,(0,1):C.GC_99})

V_92 = Vertex(name = 'V_92',
              particles = [ P.A, P.A, P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVS2, L.VVVVS4 ],
              couplings = {(0,0):C.GC_191,(0,1):C.GC_190})

V_93 = Vertex(name = 'V_93',
              particles = [ P.A, P.A, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV3, L.VVVV9 ],
              couplings = {(0,0):C.GC_207,(0,1):C.GC_206})

V_94 = Vertex(name = 'V_94',
              particles = [ P.A, P.Z, P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS10, L.VVVVSS7 ],
              couplings = {(0,0):C.GC_95,(0,1):C.GC_94})

V_95 = Vertex(name = 'V_95',
              particles = [ P.A, P.Z, P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVS5, L.VVVVS8 ],
              couplings = {(0,1):C.GC_186,(0,0):C.GC_185})

V_96 = Vertex(name = 'V_96',
              particles = [ P.A, P.Z, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV10, L.VVVV13 ],
              couplings = {(0,1):C.GC_203,(0,0):C.GC_202})

V_97 = Vertex(name = 'V_97',
              particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS14, L.VVVVSS16 ],
              couplings = {(0,0):C.GC_88,(0,1):C.GC_86})

V_98 = Vertex(name = 'V_98',
              particles = [ P.Z, P.Z, P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVS12, L.VVVVS14 ],
              couplings = {(0,0):C.GC_179,(0,1):C.GC_177})

V_99 = Vertex(name = 'V_99',
              particles = [ P.Z, P.Z, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV17, L.VVVV19 ],
              couplings = {(0,0):C.GC_197,(0,1):C.GC_195})

V_100 = Vertex(name = 'V_100',
               particles = [ P.A, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVSS1, L.VVVVVSS3, L.VVVVVSS4, L.VVVVVSS5, L.VVVVVSS7 ],
               couplings = {(0,1):C.GC_56,(0,2):C.GC_69,(0,0):C.GC_83,(0,3):C.GC_92,(0,4):C.GC_96})

V_101 = Vertex(name = 'V_101',
               particles = [ P.A, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS1, L.VVVVVS3, L.VVVVVS4, L.VVVVVS5, L.VVVVVS7 ],
               couplings = {(0,1):C.GC_131,(0,2):C.GC_137,(0,0):C.GC_143,(0,3):C.GC_183,(0,4):C.GC_187})

V_102 = Vertex(name = 'V_102',
               particles = [ P.A, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV1, L.VVVVV3, L.VVVVV4, L.VVVVV6 ],
               couplings = {(0,1):C.GC_165,(0,2):C.GC_169,(0,0):C.GC_174,(0,3):C.GC_204})

V_103 = Vertex(name = 'V_103',
               particles = [ P.A, P.A, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS2, L.VVVVVVSS4 ],
               couplings = {(0,0):C.GC_102,(0,1):C.GC_101})

V_104 = Vertex(name = 'V_104',
               particles = [ P.A, P.A, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS2, L.VVVVVVS4 ],
               couplings = {(0,0):C.GC_193,(0,1):C.GC_192})

V_105 = Vertex(name = 'V_105',
               particles = [ P.A, P.A, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV2, L.VVVVVV4 ],
               couplings = {(0,0):C.GC_209,(0,1):C.GC_208})

V_106 = Vertex(name = 'V_106',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVSS11, L.VVVVVSS12, L.VVVVVSS13, L.VVVVVSS8 ],
               couplings = {(0,2):C.GC_20,(0,1):C.GC_39,(0,0):C.GC_78,(0,3):C.GC_89})

V_107 = Vertex(name = 'V_107',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS11, L.VVVVVS12, L.VVVVVS13, L.VVVVVS8 ],
               couplings = {(0,2):C.GC_109,(0,1):C.GC_121,(0,0):C.GC_141,(0,3):C.GC_180})

V_108 = Vertex(name = 'V_108',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV10, L.VVVVV11, L.VVVVV12, L.VVVVV7 ],
               couplings = {(0,2):C.GC_148,(0,1):C.GC_158,(0,0):C.GC_172,(0,3):C.GC_198})

V_109 = Vertex(name = 'V_109',
               particles = [ P.A, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS10 ],
               couplings = {(0,0):C.GC_98})

V_110 = Vertex(name = 'V_110',
               particles = [ P.A, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS10 ],
               couplings = {(0,0):C.GC_189})

V_111 = Vertex(name = 'V_111',
               particles = [ P.A, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV10 ],
               couplings = {(0,0):C.GC_205})

V_112 = Vertex(name = 'V_112',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS3 ],
               couplings = {(0,0):C.GC_93})

V_113 = Vertex(name = 'V_113',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS3 ],
               couplings = {(0,0):C.GC_184})

V_114 = Vertex(name = 'V_114',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV3 ],
               couplings = {(0,0):C.GC_201})

V_115 = Vertex(name = 'V_115',
               particles = [ P.A, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS2 ],
               couplings = {(0,0):C.GC_104})

V_116 = Vertex(name = 'V_116',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS3 ],
               couplings = {(0,1):C.GC_125,(0,0):C.GC_134})

V_117 = Vertex(name = 'V_117',
               particles = [ P.A, P.A, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVSS16, L.VVVVVSS6 ],
               couplings = {(0,1):C.GC_90,(0,0):C.GC_97})

V_118 = Vertex(name = 'V_118',
               particles = [ P.A, P.A, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS16, L.VVVVVS6 ],
               couplings = {(0,1):C.GC_181,(0,0):C.GC_188})

V_119 = Vertex(name = 'V_119',
               particles = [ P.A, P.A, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV5 ],
               couplings = {(0,0):C.GC_199})

