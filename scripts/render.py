import sys,trimesh,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
m=trimesh.load(sys.argv[1])
parts=sorted(m.split(only_watertight=False),key=lambda p:-abs(p.volume))
cols={0:'#d9d4c7',1:'#9fb7c9',2:'#e8c36a',3:'#d9d4c7'}
def col(i): return cols.get(i, '#5c6670' if i<10 else '#c0392b')
light=np.array([0.4,-0.5,0.8]);light/=np.linalg.norm(light)
def draw(ax,elev,azim,explode=0):
    for i,p in enumerate(parts):
        v=p.vertices.copy()
        if explode and i in (1,4,5,6,7,8,9,10,12,13): v[:,1]-=explode
        tris=v[p.faces]
        n=p.face_normals; sh=0.45+0.55*np.clip(n@light,0,1)
        c=np.array(matplotlib.colors.to_rgb(col(i)))
        fc=np.clip(c[None,:]*sh[:,None],0,1)
        ax.add_collection3d(Poly3DCollection(tris,facecolors=fc,edgecolors='none',linewidths=0))
    b=m.bounds.copy(); 
    if explode: b[0,1]-=explode
    c=b.mean(0); r=(b[1]-b[0]).max()/2
    ax.set_xlim(c[0]-r,c[0]+r);ax.set_ylim(c[1]-r,c[1]+r);ax.set_zlim(c[2]-r,c[2]+r)
    ax.view_init(elev=elev,azim=azim);ax.set_axis_off();ax.set_box_aspect((1,1,1))
for name,elev,azim,ex in [('hero',18,-60,0),('side',0,0,0),('exploded',15,-55,40)]:
    fig=plt.figure(figsize=(10,10),dpi=130);fig.patch.set_facecolor('#0b0d10')
    ax=fig.add_subplot(projection='3d');ax.set_facecolor('#0b0d10')
    draw(ax,elev,azim,ex);plt.subplots_adjust(0,0,1,1)
    fig.savefig(f'{name}.png',facecolor=fig.get_facecolor());plt.close(fig);print(name)
