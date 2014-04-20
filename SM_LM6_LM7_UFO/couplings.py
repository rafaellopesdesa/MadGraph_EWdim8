# This file was automatically created by FeynRules 2.0.17
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (November 20, 2012)
# Date: Fri 21 Feb 2014 15:19:33


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = '-(FM6*complex(0,1))',
                order = {'NP':1})

GC_5 = Coupling(name = 'GC_5',
                value = '-(cw**2*FM6*complex(0,1))',
                order = {'NP':1})

GC_6 = Coupling(name = 'GC_6',
                value = '(ee**2*FM6*complex(0,1))/2.',
                order = {'NP':1,'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '(FM7*complex(0,1))/4.',
                order = {'NP':1})

GC_8 = Coupling(name = 'GC_8',
                value = '(cw**2*FM7*complex(0,1))/4.',
                order = {'NP':1})

GC_9 = Coupling(name = 'GC_9',
                value = '-(ee*FM7*complex(0,1))/8.',
                order = {'NP':1,'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '-(ee**2*FM7*complex(0,1))/8.',
                 order = {'NP':1,'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '-(ee**2*FM7*complex(0,1))/4.',
                 order = {'NP':1,'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '-G',
                 order = {'QCD':1})

GC_13 = Coupling(name = 'GC_13',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_14 = Coupling(name = 'GC_14',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_15 = Coupling(name = 'GC_15',
                 value = 'cw*complex(0,1)*gw',
                 order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = 'cw*FM6*complex(0,1)*gw',
                 order = {'NP':1,'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '(cw*FM7*complex(0,1)*gw)/4.',
                 order = {'NP':1,'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '(cw*ee*FM7*complex(0,1)*gw)/8.',
                 order = {'NP':1,'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '(ee**2*FM7*complex(0,1)*gw)/(8.*cw)',
                 order = {'NP':1,'QED':3})

GC_20 = Coupling(name = 'GC_20',
                 value = '(cw*ee**2*FM7*complex(0,1)*gw)/2.',
                 order = {'NP':1,'QED':3})

GC_21 = Coupling(name = 'GC_21',
                 value = '-(complex(0,1)*gw**2)',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = 'cw**2*complex(0,1)*gw**2',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '-(FM6*complex(0,1)*gw**2)',
                 order = {'NP':1,'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = 'cw**2*FM6*complex(0,1)*gw**2',
                 order = {'NP':1,'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '-(ee**2*FM6*complex(0,1)*gw**2)/2.',
                 order = {'NP':1,'QED':4})

GC_26 = Coupling(name = 'GC_26',
                 value = '(FM7*complex(0,1)*gw**2)/2.',
                 order = {'NP':1,'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '-(cw**2*FM7*complex(0,1)*gw**2)/2.',
                 order = {'NP':1,'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '-(ee**2*FM7*complex(0,1)*gw**2)',
                 order = {'NP':1,'QED':4})

GC_29 = Coupling(name = 'GC_29',
                 value = '(-3*ee**2*FM7*complex(0,1)*gw**2)/2.',
                 order = {'NP':1,'QED':4})

GC_30 = Coupling(name = 'GC_30',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '(3*ee**2*FM6*complex(0,1)*gw**2)/(2.*sw**2) + (3*ee**2*FM7*complex(0,1)*gw**2)/(4.*sw**2)',
                 order = {'NP':1,'QED':4})

GC_32 = Coupling(name = 'GC_32',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '(ee**2*FM6*complex(0,1))/(2.*sw**2)',
                 order = {'NP':1,'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '(cw**2*ee**2*FM6*complex(0,1))/(2.*sw**2)',
                 order = {'NP':1,'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '(ee**2*FM7*complex(0,1))/(4.*sw**2)',
                 order = {'NP':1,'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '-(cw**2*ee**2*FM7*complex(0,1))/(8.*sw**2)',
                 order = {'NP':1,'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '-(cw*ee**2*FM6*complex(0,1)*gw)/(2.*sw**2)',
                 order = {'NP':1,'QED':3})

GC_38 = Coupling(name = 'GC_38',
                 value = '(cw*ee**2*FM7*complex(0,1)*gw)/(8.*sw**2)',
                 order = {'NP':1,'QED':3})

GC_39 = Coupling(name = 'GC_39',
                 value = '(3*cw**3*ee**2*FM7*complex(0,1)*gw)/(8.*sw**2)',
                 order = {'NP':1,'QED':3})

GC_40 = Coupling(name = 'GC_40',
                 value = '-(cw**2*ee**2*FM6*complex(0,1)*gw**2)/(2.*sw**2)',
                 order = {'NP':1,'QED':4})

GC_41 = Coupling(name = 'GC_41',
                 value = '(-9*cw**2*ee**2*FM7*complex(0,1)*gw**2)/(4.*sw**2)',
                 order = {'NP':1,'QED':4})

GC_42 = Coupling(name = 'GC_42',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '(cw*ee**2*FM6*complex(0,1))/(2.*sw)',
                 order = {'NP':1,'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '-(cw*ee*FM7*complex(0,1))/(8.*sw)',
                 order = {'NP':1,'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '(cw*ee**2*FM7*complex(0,1))/(8.*sw)',
                 order = {'NP':1,'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '-(ee**2*FM6*complex(0,1)*gw)/(2.*sw)',
                 order = {'NP':1,'QED':3})

GC_53 = Coupling(name = 'GC_53',
                 value = '(ee*FM7*complex(0,1)*gw)/(8.*sw)',
                 order = {'NP':1,'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '-(cw**2*ee*FM7*complex(0,1)*gw)/(8.*sw)',
                 order = {'NP':1,'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '(ee**2*FM7*complex(0,1)*gw)/(4.*sw)',
                 order = {'NP':1,'QED':3})

GC_56 = Coupling(name = 'GC_56',
                 value = '-(cw**2*ee**2*FM7*complex(0,1)*gw)/(8.*sw)',
                 order = {'NP':1,'QED':3})

GC_57 = Coupling(name = 'GC_57',
                 value = '(2*cw*ee**2*FM6*complex(0,1)*gw**2)/sw',
                 order = {'NP':1,'QED':4})

GC_58 = Coupling(name = 'GC_58',
                 value = '-(cw*ee**2*FM7*complex(0,1)*gw**2)/(2.*sw)',
                 order = {'NP':1,'QED':4})

GC_59 = Coupling(name = 'GC_59',
                 value = '-(ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(cw*FM6*complex(0,1)*sw)',
                 order = {'NP':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '(cw*FM7*complex(0,1)*sw)/4.',
                 order = {'NP':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-(ee*FM7*complex(0,1)*sw)/(8.*cw)',
                 order = {'NP':1,'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '(ee**2*FM7*complex(0,1)*sw)/(8.*cw)',
                 order = {'NP':1,'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = 'complex(0,1)*gw*sw',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = 'FM6*complex(0,1)*gw*sw',
                 order = {'NP':1,'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(FM7*complex(0,1)*gw*sw)/4.',
                 order = {'NP':1,'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-(ee*FM7*complex(0,1)*gw*sw)/8.',
                 order = {'NP':1,'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '-(ee**2*FM7*complex(0,1)*gw*sw)/4.',
                 order = {'NP':1,'QED':3})

GC_70 = Coupling(name = 'GC_70',
                 value = '-2*cw*complex(0,1)*gw**2*sw',
                 order = {'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '-2*cw*FM6*complex(0,1)*gw**2*sw',
                 order = {'NP':1,'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '(cw*FM7*complex(0,1)*gw**2*sw)/4.',
                 order = {'NP':1,'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '-(ee**2*FM7*complex(0,1)*gw**2*sw)/(2.*cw)',
                 order = {'NP':1,'QED':4})

GC_74 = Coupling(name = 'GC_74',
                 value = '-(FM6*complex(0,1)*sw**2)',
                 order = {'NP':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '(FM7*complex(0,1)*sw**2)/4.',
                 order = {'NP':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-(ee**2*FM7*complex(0,1)*sw**2)/(8.*cw**2)',
                 order = {'NP':1,'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = '(ee*FM7*complex(0,1)*gw*sw**2)/(8.*cw)',
                 order = {'NP':1,'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '(ee**2*FM7*complex(0,1)*gw*sw**2)/(8.*cw)',
                 order = {'NP':1,'QED':3})

GC_79 = Coupling(name = 'GC_79',
                 value = 'complex(0,1)*gw**2*sw**2',
                 order = {'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = 'FM6*complex(0,1)*gw**2*sw**2',
                 order = {'NP':1,'QED':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '-(FM7*complex(0,1)*gw**2*sw**2)/2.',
                 order = {'NP':1,'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '-(ee**2*FM7*complex(0,1)*gw**2*sw**2)/(4.*cw**2)',
                 order = {'NP':1,'QED':4})

GC_83 = Coupling(name = 'GC_83',
                 value = '-(ee**2*FM7*complex(0,1)*gw*sw**3)/(8.*cw**2)',
                 order = {'NP':1,'QED':3})

GC_84 = Coupling(name = 'GC_84',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = 'cw**2*ee**2*FM6*complex(0,1) + (cw**4*ee**2*FM6*complex(0,1))/(2.*sw**2) + (ee**2*FM6*complex(0,1)*sw**2)/2.',
                 order = {'NP':1,'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = 'ee**2*FM6*complex(0,1) + (ee**2*FM6*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'NP':1,'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '-(cw**2*ee**2*FM7*complex(0,1))/4. - (cw**4*ee**2*FM7*complex(0,1))/(8.*sw**2) - (ee**2*FM7*complex(0,1)*sw**2)/8.',
                 order = {'NP':1,'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '-(cw*ee**2*FM6*complex(0,1)*gw) - (cw**3*ee**2*FM6*complex(0,1)*gw)/(2.*sw**2) - (ee**2*FM6*complex(0,1)*gw*sw**2)/(2.*cw)',
                 order = {'NP':1,'QED':3})

GC_90 = Coupling(name = 'GC_90',
                 value = '(cw*ee**2*FM7*complex(0,1)*gw)/8. + (ee**2*FM7*complex(0,1)*gw*sw**2)/(8.*cw)',
                 order = {'NP':1,'QED':3})

GC_91 = Coupling(name = 'GC_91',
                 value = 'ee**2*FM6*complex(0,1)*gw**2 + (ee**2*FM6*complex(0,1)*gw**2*sw**2)/(2.*cw**2)',
                 order = {'NP':1,'QED':4})

GC_92 = Coupling(name = 'GC_92',
                 value = '-(cw**2*ee*FM7*complex(0,1)*gw**2)/8. - (ee*FM7*complex(0,1)*gw**2*sw**2)/8.',
                 order = {'NP':1,'QED':3})

GC_93 = Coupling(name = 'GC_93',
                 value = '-(cw**2*ee**2*FM6*complex(0,1)*gw**2) - (cw**2*ee**2*FM7*complex(0,1)*gw**2)/2. - (cw**4*ee**2*FM6*complex(0,1)*gw**2)/(2.*sw**2) - (cw**4*ee**2*FM7*complex(0,1)*gw**2)/(4.*sw**2) - (ee**2*FM6*complex(0,1)*gw**2*sw**2)/2. - (ee**2*FM7*complex(0,1)*gw**2*sw**2)/4.',
                 order = {'NP':1,'QED':4})

GC_94 = Coupling(name = 'GC_94',
                 value = '(cw**3*ee**2*FM6*complex(0,1))/(2.*sw) + cw*ee**2*FM6*complex(0,1)*sw + (ee**2*FM6*complex(0,1)*sw**3)/(2.*cw)',
                 order = {'NP':1,'QED':2})

GC_95 = Coupling(name = 'GC_95',
                 value = '-(cw**3*ee**2*FM7*complex(0,1))/(8.*sw) - (cw*ee**2*FM7*complex(0,1)*sw)/4. - (ee**2*FM7*complex(0,1)*sw**3)/(8.*cw)',
                 order = {'NP':1,'QED':2})

GC_96 = Coupling(name = 'GC_96',
                 value = '-(cw**2*ee**2*FM6*complex(0,1)*gw)/(2.*sw) - ee**2*FM6*complex(0,1)*gw*sw - (ee**2*FM6*complex(0,1)*gw*sw**3)/(2.*cw**2)',
                 order = {'NP':1,'QED':3})

GC_97 = Coupling(name = 'GC_97',
                 value = '-(cw*ee*FM7*complex(0,1)*gw**2*sw)/8. - (ee*FM7*complex(0,1)*gw**2*sw**3)/(8.*cw)',
                 order = {'NP':1,'QED':3})

GC_98 = Coupling(name = 'GC_98',
                 value = '(cw**3*ee**2*FM6*complex(0,1)*gw**2)/sw + (cw**3*ee**2*FM7*complex(0,1)*gw**2)/(2.*sw) + 2*cw*ee**2*FM6*complex(0,1)*gw**2*sw + cw*ee**2*FM7*complex(0,1)*gw**2*sw + (ee**2*FM6*complex(0,1)*gw**2*sw**3)/cw + (ee**2*FM7*complex(0,1)*gw**2*sw**3)/(2.*cw)',
                 order = {'NP':1,'QED':4})

GC_99 = Coupling(name = 'GC_99',
                 value = '(cw**2*ee**2*FM6*complex(0,1))/2. + ee**2*FM6*complex(0,1)*sw**2 + (ee**2*FM6*complex(0,1)*sw**4)/(2.*cw**2)',
                 order = {'NP':1,'QED':2})

GC_100 = Coupling(name = 'GC_100',
                  value = '-(cw**2*ee**2*FM7*complex(0,1))/8. - (ee**2*FM7*complex(0,1)*sw**2)/4. - (ee**2*FM7*complex(0,1)*sw**4)/(8.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_101 = Coupling(name = 'GC_101',
                  value = '-(cw**2*ee**2*FM6*complex(0,1)*gw**2)/2. - ee**2*FM6*complex(0,1)*gw**2*sw**2 - (ee**2*FM6*complex(0,1)*gw**2*sw**4)/(2.*cw**2)',
                  order = {'NP':1,'QED':4})

GC_102 = Coupling(name = 'GC_102',
                  value = '(cw**2*ee**2*FM7*complex(0,1)*gw**2)/4. + (ee**2*FM7*complex(0,1)*gw**2*sw**2)/2. + (ee**2*FM7*complex(0,1)*gw**2*sw**4)/(4.*cw**2)',
                  order = {'NP':1,'QED':4})

GC_103 = Coupling(name = 'GC_103',
                  value = '(ee**2*FM6*complex(0,1)*v)/2.',
                  order = {'NP':1,'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '-(ee*FM7*complex(0,1)*v)/8.',
                  order = {'NP':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '-(ee**2*FM7*complex(0,1)*v)/8.',
                  order = {'NP':1,'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '-(ee**2*FM7*complex(0,1)*v)/4.',
                  order = {'NP':1,'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '(cw*ee*FM7*complex(0,1)*gw*v)/8.',
                  order = {'NP':1,'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '(ee**2*FM7*complex(0,1)*gw*v)/(8.*cw)',
                  order = {'NP':1,'QED':2})

GC_109 = Coupling(name = 'GC_109',
                  value = '(cw*ee**2*FM7*complex(0,1)*gw*v)/2.',
                  order = {'NP':1,'QED':2})

GC_110 = Coupling(name = 'GC_110',
                  value = '-(ee**2*FM6*complex(0,1)*gw**2*v)/2.',
                  order = {'NP':1,'QED':3})

GC_111 = Coupling(name = 'GC_111',
                  value = '-(ee**2*FM7*complex(0,1)*gw**2*v)',
                  order = {'NP':1,'QED':3})

GC_112 = Coupling(name = 'GC_112',
                  value = '(-3*ee**2*FM7*complex(0,1)*gw**2*v)/2.',
                  order = {'NP':1,'QED':3})

GC_113 = Coupling(name = 'GC_113',
                  value = '-6*complex(0,1)*lam*v',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '(ee**2*complex(0,1)*v)/(2.*sw**2)',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '(ee**2*FM6*complex(0,1)*v)/(2.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '(cw**2*ee**2*FM6*complex(0,1)*v)/(2.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '(ee**2*FM7*complex(0,1)*v)/(4.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*v)/(8.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '-(cw*ee**2*FM6*complex(0,1)*gw*v)/(2.*sw**2)',
                  order = {'NP':1,'QED':2})

GC_120 = Coupling(name = 'GC_120',
                  value = '(cw*ee**2*FM7*complex(0,1)*gw*v)/(8.*sw**2)',
                  order = {'NP':1,'QED':2})

GC_121 = Coupling(name = 'GC_121',
                  value = '(3*cw**3*ee**2*FM7*complex(0,1)*gw*v)/(8.*sw**2)',
                  order = {'NP':1,'QED':2})

GC_122 = Coupling(name = 'GC_122',
                  value = '-(cw**2*ee**2*FM6*complex(0,1)*gw**2*v)/(2.*sw**2)',
                  order = {'NP':1,'QED':3})

GC_123 = Coupling(name = 'GC_123',
                  value = '(-9*cw**2*ee**2*FM7*complex(0,1)*gw**2*v)/(4.*sw**2)',
                  order = {'NP':1,'QED':3})

GC_124 = Coupling(name = 'GC_124',
                  value = '(cw*ee**2*FM6*complex(0,1)*v)/(2.*sw)',
                  order = {'NP':1,'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '-(cw*ee*FM7*complex(0,1)*v)/(8.*sw)',
                  order = {'NP':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '(cw*ee**2*FM7*complex(0,1)*v)/(8.*sw)',
                  order = {'NP':1,'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '-(ee**2*FM6*complex(0,1)*gw*v)/(2.*sw)',
                  order = {'NP':1,'QED':2})

GC_128 = Coupling(name = 'GC_128',
                  value = '(ee*FM7*complex(0,1)*gw*v)/(8.*sw)',
                  order = {'NP':1,'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '-(cw**2*ee*FM7*complex(0,1)*gw*v)/(8.*sw)',
                  order = {'NP':1,'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(ee**2*FM7*complex(0,1)*gw*v)/(4.*sw)',
                  order = {'NP':1,'QED':2})

GC_131 = Coupling(name = 'GC_131',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*gw*v)/(8.*sw)',
                  order = {'NP':1,'QED':2})

GC_132 = Coupling(name = 'GC_132',
                  value = '(2*cw*ee**2*FM6*complex(0,1)*gw**2*v)/sw',
                  order = {'NP':1,'QED':3})

GC_133 = Coupling(name = 'GC_133',
                  value = '-(cw*ee**2*FM7*complex(0,1)*gw**2*v)/(2.*sw)',
                  order = {'NP':1,'QED':3})

GC_134 = Coupling(name = 'GC_134',
                  value = '-(ee*FM7*complex(0,1)*sw*v)/(8.*cw)',
                  order = {'NP':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '(ee**2*FM7*complex(0,1)*sw*v)/(8.*cw)',
                  order = {'NP':1,'QED':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '-(ee*FM7*complex(0,1)*gw*sw*v)/8.',
                  order = {'NP':1,'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '-(ee**2*FM7*complex(0,1)*gw*sw*v)/4.',
                  order = {'NP':1,'QED':2})

GC_138 = Coupling(name = 'GC_138',
                  value = '-(ee**2*FM7*complex(0,1)*gw**2*sw*v)/(2.*cw)',
                  order = {'NP':1,'QED':3})

GC_139 = Coupling(name = 'GC_139',
                  value = '-(ee**2*FM7*complex(0,1)*sw**2*v)/(8.*cw**2)',
                  order = {'NP':1,'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '(ee*FM7*complex(0,1)*gw*sw**2*v)/(8.*cw)',
                  order = {'NP':1,'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '(ee**2*FM7*complex(0,1)*gw*sw**2*v)/(8.*cw)',
                  order = {'NP':1,'QED':2})

GC_142 = Coupling(name = 'GC_142',
                  value = '-(ee**2*FM7*complex(0,1)*gw**2*sw**2*v)/(4.*cw**2)',
                  order = {'NP':1,'QED':3})

GC_143 = Coupling(name = 'GC_143',
                  value = '-(ee**2*FM7*complex(0,1)*gw*sw**3*v)/(8.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_144 = Coupling(name = 'GC_144',
                  value = '(ee**2*FM6*complex(0,1)*v**2)/4.',
                  order = {'NP':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '-(ee**2*FM7*complex(0,1)*v**2)/16.',
                  order = {'NP':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '-(ee**2*FM7*complex(0,1)*v**2)/8.',
                  order = {'NP':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '(ee**2*FM7*complex(0,1)*gw*v**2)/(16.*cw)',
                  order = {'NP':1,'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '(cw*ee**2*FM7*complex(0,1)*gw*v**2)/4.',
                  order = {'NP':1,'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '-(ee**2*FM6*complex(0,1)*gw**2*v**2)/4.',
                  order = {'NP':1,'QED':2})

GC_150 = Coupling(name = 'GC_150',
                  value = '-(ee**2*FM7*complex(0,1)*gw**2*v**2)/2.',
                  order = {'NP':1,'QED':2})

GC_151 = Coupling(name = 'GC_151',
                  value = '(-3*ee**2*FM7*complex(0,1)*gw**2*v**2)/4.',
                  order = {'NP':1,'QED':2})

GC_152 = Coupling(name = 'GC_152',
                  value = '(ee**2*FM6*complex(0,1)*v**2)/(4.*sw**2)',
                  order = {'NP':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '(cw**2*ee**2*FM6*complex(0,1)*v**2)/(4.*sw**2)',
                  order = {'NP':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '(ee**2*FM7*complex(0,1)*v**2)/(8.*sw**2)',
                  order = {'NP':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*v**2)/(16.*sw**2)',
                  order = {'NP':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '-(cw*ee**2*FM6*complex(0,1)*gw*v**2)/(4.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '(cw*ee**2*FM7*complex(0,1)*gw*v**2)/(16.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '(3*cw**3*ee**2*FM7*complex(0,1)*gw*v**2)/(16.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '-(cw**2*ee**2*FM6*complex(0,1)*gw**2*v**2)/(4.*sw**2)',
                  order = {'NP':1,'QED':2})

GC_160 = Coupling(name = 'GC_160',
                  value = '(-9*cw**2*ee**2*FM7*complex(0,1)*gw**2*v**2)/(8.*sw**2)',
                  order = {'NP':1,'QED':2})

GC_161 = Coupling(name = 'GC_161',
                  value = '(cw*ee**2*FM6*complex(0,1)*v**2)/(4.*sw)',
                  order = {'NP':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '(cw*ee**2*FM7*complex(0,1)*v**2)/(16.*sw)',
                  order = {'NP':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '-(ee**2*FM6*complex(0,1)*gw*v**2)/(4.*sw)',
                  order = {'NP':1,'QED':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '(ee**2*FM7*complex(0,1)*gw*v**2)/(8.*sw)',
                  order = {'NP':1,'QED':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*gw*v**2)/(16.*sw)',
                  order = {'NP':1,'QED':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '(cw*ee**2*FM6*complex(0,1)*gw**2*v**2)/sw',
                  order = {'NP':1,'QED':2})

GC_167 = Coupling(name = 'GC_167',
                  value = '-(cw*ee**2*FM7*complex(0,1)*gw**2*v**2)/(4.*sw)',
                  order = {'NP':1,'QED':2})

GC_168 = Coupling(name = 'GC_168',
                  value = '(ee**2*FM7*complex(0,1)*sw*v**2)/(16.*cw)',
                  order = {'NP':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '-(ee**2*FM7*complex(0,1)*gw*sw*v**2)/8.',
                  order = {'NP':1,'QED':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '-(ee**2*FM7*complex(0,1)*gw**2*sw*v**2)/(4.*cw)',
                  order = {'NP':1,'QED':2})

GC_171 = Coupling(name = 'GC_171',
                  value = '-(ee**2*FM7*complex(0,1)*sw**2*v**2)/(16.*cw**2)',
                  order = {'NP':1})

GC_172 = Coupling(name = 'GC_172',
                  value = '(ee**2*FM7*complex(0,1)*gw*sw**2*v**2)/(16.*cw)',
                  order = {'NP':1,'QED':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '-(ee**2*FM7*complex(0,1)*gw**2*sw**2*v**2)/(8.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_174 = Coupling(name = 'GC_174',
                  value = '-(ee**2*FM7*complex(0,1)*gw*sw**3*v**2)/(16.*cw**2)',
                  order = {'NP':1,'QED':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '(3*ee**2*FM6*complex(0,1)*gw**2*v)/(2.*sw**2) + (3*ee**2*FM7*complex(0,1)*gw**2*v)/(4.*sw**2)',
                  order = {'NP':1,'QED':3})

GC_176 = Coupling(name = 'GC_176',
                  value = 'ee**2*complex(0,1)*v + (cw**2*ee**2*complex(0,1)*v)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*v)/(2.*cw**2)',
                  order = {'QED':1})

GC_177 = Coupling(name = 'GC_177',
                  value = 'cw**2*ee**2*FM6*complex(0,1)*v + (cw**4*ee**2*FM6*complex(0,1)*v)/(2.*sw**2) + (ee**2*FM6*complex(0,1)*sw**2*v)/2.',
                  order = {'NP':1,'QED':1})

GC_178 = Coupling(name = 'GC_178',
                  value = 'ee**2*FM6*complex(0,1)*v + (ee**2*FM6*complex(0,1)*sw**2*v)/(2.*cw**2)',
                  order = {'NP':1,'QED':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*v)/4. - (cw**4*ee**2*FM7*complex(0,1)*v)/(8.*sw**2) - (ee**2*FM7*complex(0,1)*sw**2*v)/8.',
                  order = {'NP':1,'QED':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '-(cw*ee**2*FM6*complex(0,1)*gw*v) - (cw**3*ee**2*FM6*complex(0,1)*gw*v)/(2.*sw**2) - (ee**2*FM6*complex(0,1)*gw*sw**2*v)/(2.*cw)',
                  order = {'NP':1,'QED':2})

GC_181 = Coupling(name = 'GC_181',
                  value = '(cw*ee**2*FM7*complex(0,1)*gw*v)/8. + (ee**2*FM7*complex(0,1)*gw*sw**2*v)/(8.*cw)',
                  order = {'NP':1,'QED':2})

GC_182 = Coupling(name = 'GC_182',
                  value = 'ee**2*FM6*complex(0,1)*gw**2*v + (ee**2*FM6*complex(0,1)*gw**2*sw**2*v)/(2.*cw**2)',
                  order = {'NP':1,'QED':3})

GC_183 = Coupling(name = 'GC_183',
                  value = '-(cw**2*ee*FM7*complex(0,1)*gw**2*v)/8. - (ee*FM7*complex(0,1)*gw**2*sw**2*v)/8.',
                  order = {'NP':1,'QED':2})

GC_184 = Coupling(name = 'GC_184',
                  value = '-(cw**2*ee**2*FM6*complex(0,1)*gw**2*v) - (cw**2*ee**2*FM7*complex(0,1)*gw**2*v)/2. - (cw**4*ee**2*FM6*complex(0,1)*gw**2*v)/(2.*sw**2) - (cw**4*ee**2*FM7*complex(0,1)*gw**2*v)/(4.*sw**2) - (ee**2*FM6*complex(0,1)*gw**2*sw**2*v)/2. - (ee**2*FM7*complex(0,1)*gw**2*sw**2*v)/4.',
                  order = {'NP':1,'QED':3})

GC_185 = Coupling(name = 'GC_185',
                  value = '(cw**3*ee**2*FM6*complex(0,1)*v)/(2.*sw) + cw*ee**2*FM6*complex(0,1)*sw*v + (ee**2*FM6*complex(0,1)*sw**3*v)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_186 = Coupling(name = 'GC_186',
                  value = '-(cw**3*ee**2*FM7*complex(0,1)*v)/(8.*sw) - (cw*ee**2*FM7*complex(0,1)*sw*v)/4. - (ee**2*FM7*complex(0,1)*sw**3*v)/(8.*cw)',
                  order = {'NP':1,'QED':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '-(cw**2*ee**2*FM6*complex(0,1)*gw*v)/(2.*sw) - ee**2*FM6*complex(0,1)*gw*sw*v - (ee**2*FM6*complex(0,1)*gw*sw**3*v)/(2.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_188 = Coupling(name = 'GC_188',
                  value = '-(cw*ee*FM7*complex(0,1)*gw**2*sw*v)/8. - (ee*FM7*complex(0,1)*gw**2*sw**3*v)/(8.*cw)',
                  order = {'NP':1,'QED':2})

GC_189 = Coupling(name = 'GC_189',
                  value = '(cw**3*ee**2*FM6*complex(0,1)*gw**2*v)/sw + (cw**3*ee**2*FM7*complex(0,1)*gw**2*v)/(2.*sw) + 2*cw*ee**2*FM6*complex(0,1)*gw**2*sw*v + cw*ee**2*FM7*complex(0,1)*gw**2*sw*v + (ee**2*FM6*complex(0,1)*gw**2*sw**3*v)/cw + (ee**2*FM7*complex(0,1)*gw**2*sw**3*v)/(2.*cw)',
                  order = {'NP':1,'QED':3})

GC_190 = Coupling(name = 'GC_190',
                  value = '(cw**2*ee**2*FM6*complex(0,1)*v)/2. + ee**2*FM6*complex(0,1)*sw**2*v + (ee**2*FM6*complex(0,1)*sw**4*v)/(2.*cw**2)',
                  order = {'NP':1,'QED':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*v)/8. - (ee**2*FM7*complex(0,1)*sw**2*v)/4. - (ee**2*FM7*complex(0,1)*sw**4*v)/(8.*cw**2)',
                  order = {'NP':1,'QED':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '-(cw**2*ee**2*FM6*complex(0,1)*gw**2*v)/2. - ee**2*FM6*complex(0,1)*gw**2*sw**2*v - (ee**2*FM6*complex(0,1)*gw**2*sw**4*v)/(2.*cw**2)',
                  order = {'NP':1,'QED':3})

GC_193 = Coupling(name = 'GC_193',
                  value = '(cw**2*ee**2*FM7*complex(0,1)*gw**2*v)/4. + (ee**2*FM7*complex(0,1)*gw**2*sw**2*v)/2. + (ee**2*FM7*complex(0,1)*gw**2*sw**4*v)/(4.*cw**2)',
                  order = {'NP':1,'QED':3})

GC_194 = Coupling(name = 'GC_194',
                  value = '(3*ee**2*FM6*complex(0,1)*gw**2*v**2)/(4.*sw**2) + (3*ee**2*FM7*complex(0,1)*gw**2*v**2)/(8.*sw**2)',
                  order = {'NP':1,'QED':2})

GC_195 = Coupling(name = 'GC_195',
                  value = '(cw**2*ee**2*FM6*complex(0,1)*v**2)/2. + (cw**4*ee**2*FM6*complex(0,1)*v**2)/(4.*sw**2) + (ee**2*FM6*complex(0,1)*sw**2*v**2)/4.',
                  order = {'NP':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '(ee**2*FM6*complex(0,1)*v**2)/2. + (ee**2*FM6*complex(0,1)*sw**2*v**2)/(4.*cw**2)',
                  order = {'NP':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*v**2)/8. - (cw**4*ee**2*FM7*complex(0,1)*v**2)/(16.*sw**2) - (ee**2*FM7*complex(0,1)*sw**2*v**2)/16.',
                  order = {'NP':1})

GC_198 = Coupling(name = 'GC_198',
                  value = '-(cw*ee**2*FM6*complex(0,1)*gw*v**2)/2. - (cw**3*ee**2*FM6*complex(0,1)*gw*v**2)/(4.*sw**2) - (ee**2*FM6*complex(0,1)*gw*sw**2*v**2)/(4.*cw)',
                  order = {'NP':1,'QED':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '(cw*ee**2*FM7*complex(0,1)*gw*v**2)/16. + (ee**2*FM7*complex(0,1)*gw*sw**2*v**2)/(16.*cw)',
                  order = {'NP':1,'QED':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '(ee**2*FM6*complex(0,1)*gw**2*v**2)/2. + (ee**2*FM6*complex(0,1)*gw**2*sw**2*v**2)/(4.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_201 = Coupling(name = 'GC_201',
                  value = '-(cw**2*ee**2*FM6*complex(0,1)*gw**2*v**2)/2. - (cw**2*ee**2*FM7*complex(0,1)*gw**2*v**2)/4. - (cw**4*ee**2*FM6*complex(0,1)*gw**2*v**2)/(4.*sw**2) - (cw**4*ee**2*FM7*complex(0,1)*gw**2*v**2)/(8.*sw**2) - (ee**2*FM6*complex(0,1)*gw**2*sw**2*v**2)/4. - (ee**2*FM7*complex(0,1)*gw**2*sw**2*v**2)/8.',
                  order = {'NP':1,'QED':2})

GC_202 = Coupling(name = 'GC_202',
                  value = '(cw**3*ee**2*FM6*complex(0,1)*v**2)/(4.*sw) + (cw*ee**2*FM6*complex(0,1)*sw*v**2)/2. + (ee**2*FM6*complex(0,1)*sw**3*v**2)/(4.*cw)',
                  order = {'NP':1})

GC_203 = Coupling(name = 'GC_203',
                  value = '-(cw**3*ee**2*FM7*complex(0,1)*v**2)/(16.*sw) - (cw*ee**2*FM7*complex(0,1)*sw*v**2)/8. - (ee**2*FM7*complex(0,1)*sw**3*v**2)/(16.*cw)',
                  order = {'NP':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '-(cw**2*ee**2*FM6*complex(0,1)*gw*v**2)/(4.*sw) - (ee**2*FM6*complex(0,1)*gw*sw*v**2)/2. - (ee**2*FM6*complex(0,1)*gw*sw**3*v**2)/(4.*cw**2)',
                  order = {'NP':1,'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '(cw**3*ee**2*FM6*complex(0,1)*gw**2*v**2)/(2.*sw) + (cw**3*ee**2*FM7*complex(0,1)*gw**2*v**2)/(4.*sw) + cw*ee**2*FM6*complex(0,1)*gw**2*sw*v**2 + (cw*ee**2*FM7*complex(0,1)*gw**2*sw*v**2)/2. + (ee**2*FM6*complex(0,1)*gw**2*sw**3*v**2)/(2.*cw) + (ee**2*FM7*complex(0,1)*gw**2*sw**3*v**2)/(4.*cw)',
                  order = {'NP':1,'QED':2})

GC_206 = Coupling(name = 'GC_206',
                  value = '(cw**2*ee**2*FM6*complex(0,1)*v**2)/4. + (ee**2*FM6*complex(0,1)*sw**2*v**2)/2. + (ee**2*FM6*complex(0,1)*sw**4*v**2)/(4.*cw**2)',
                  order = {'NP':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*v**2)/16. - (ee**2*FM7*complex(0,1)*sw**2*v**2)/8. - (ee**2*FM7*complex(0,1)*sw**4*v**2)/(16.*cw**2)',
                  order = {'NP':1})

GC_208 = Coupling(name = 'GC_208',
                  value = '-(cw**2*ee**2*FM6*complex(0,1)*gw**2*v**2)/4. - (ee**2*FM6*complex(0,1)*gw**2*sw**2*v**2)/2. - (ee**2*FM6*complex(0,1)*gw**2*sw**4*v**2)/(4.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_209 = Coupling(name = 'GC_209',
                  value = '(cw**2*ee**2*FM7*complex(0,1)*gw**2*v**2)/8. + (ee**2*FM7*complex(0,1)*gw**2*sw**2*v**2)/4. + (ee**2*FM7*complex(0,1)*gw**2*sw**4*v**2)/(8.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_210 = Coupling(name = 'GC_210',
                  value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_212 = Coupling(name = 'GC_212',
                  value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

