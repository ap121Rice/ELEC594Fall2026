import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.edgecolor':'#444',
                     'axes.linewidth':0.8,'savefig.dpi':220})
FP16='#6E7B8B'; INT8='#9E2B25'

fig, ax = plt.subplots(1,3, figsize=(9.2,2.55))

# (a) accuracy grouped
labels=['Precision','Recall']; x=np.arange(2); w=0.36
ax[0].bar(x-w/2,[0.752,0.534],w,label='FP16',color=FP16)
ax[0].bar(x+w/2,[0.743,0.540],w,label='INT8',color=INT8)
for i,(a,b) in enumerate(zip([0.752,0.534],[0.743,0.540])):
    ax[0].text(i-w/2,a+0.015,f'{a:.3f}',ha='center',fontsize=7.5)
    ax[0].text(i+w/2,b+0.015,f'{b:.3f}',ha='center',fontsize=7.5)
ax[0].set_xticks(x); ax[0].set_xticklabels(labels); ax[0].set_ylim(0,0.9)
ax[0].set_ylabel('Score (higher is better)'); ax[0].set_title('(a) Accuracy preserved',fontsize=9.5)
ax[0].legend(frameon=False,fontsize=8,loc='upper right'); ax[0].grid(axis='y',color='#E6E6E6',lw=0.8)
ax[0].set_axisbelow(True)

# (b) size
ax[1].bar(['FP16','INT8'],[9.9,2.6],color=[FP16,INT8],width=0.55)
for i,v in enumerate([9.9,2.6]): ax[1].text(i,v+0.2,f'{v} MB',ha='center',fontsize=8,fontweight='bold')
ax[1].set_ylim(0,11); ax[1].set_ylabel('Model size (MB)'); ax[1].set_title('(b) Model size  (-74%)',fontsize=9.5)
ax[1].grid(axis='y',color='#E6E6E6',lw=0.8); ax[1].set_axisbelow(True)

# (c) speed
ax[2].bar(['FP16','INT8'],[16.5,5.2],color=[FP16,INT8],width=0.55)
for i,v in enumerate([16.5,5.2]): ax[2].text(i,v+0.35,f'{v} ms',ha='center',fontsize=8,fontweight='bold')
ax[2].set_ylim(0,18.5); ax[2].set_ylabel('Inference time (ms/image)'); ax[2].set_title(r'(c) Inference speed  (3.2$\times$ faster)',fontsize=9.5)
ax[2].grid(axis='y',color='#E6E6E6',lw=0.8); ax[2].set_axisbelow(True)

for a in ax: a.spines['top'].set_visible(False); a.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('figures/quantization.png',bbox_inches='tight')
print('saved figures/quantization.png')
