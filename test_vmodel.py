import vmodel
import numpy as np

# m=vmodel.model1d(VsvArr=np.array([0], dtype=np.float32), VpvArr=np.array([0], dtype=np.float32),
            # VshArr=np.array([0],dtype=np.float32), VphArr=np.array([0],dtype=np.float32), etaArr=np.array([0],dtype=np.float32), rhoArr=np.array([0],dtype=np.float32), isotropic=True)
m   = vmodel.model1d()
# m1   = vmodel.model1d()


# m.get_radius(1000., 1.)
# m=vmodel.read_model(m, 'ak135.txt')

m.model_ak135_cps()
# m1.model_ak135_cps()
# 
# m.trim(200.)
# m1.trim(200.)
# m=vmodel.read_axisem_bm(m, '/home/leon/code/axisem/SOLVER/MESHES/prem_aniso_10s/1dmodel_axisem.bm')
m.add_perturb_layer_love(0., 20., 0, -0.1, True)

m.init_dip_strike()
m.init_etensor()
m.dipArr[-1] = 30.; m.dipArr[-2] = 30.
cij = m.CijArr[:,:,-1].copy()

m.rot_dip_strike()
m.decompose()