# libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
# width of the bars
barWidth = 0.3

round_robin_result_caching = [71, 881, 86, 960, 74]
CSD_result_caching = [56, 862, 69, 875, 58]
CCBS_result_caching = [95, 549, 104, 581, 97]

# FoC
cacheInControllerSize4 = [59, 647, 73, 684, 62]
cacheInControllerSize5 = [66, 809, 79, 825, 69]
cacheInControllerSize8 = [49, 616, 60, 649, 52]
cacheInControllerSize10 = [58, 540, 70, 620, 61]

# TAHC
cacheSchedulerSize5 = [70, 726, 83, 764, 73]
cacheSchedulerSize10 = [68, 696, 79, 716, 71]

# Batch servicing in TAHC
batchIncacheSchedulerSize5 = [97, 643, 101, 676, 98]

# Content caching
round_robin_content_caching = [58, 410, 73, 416, 60]
CSD_content_caching = [59, 398, 75, 413, 61]
CCBS_content_caching = [57, 315, 74, 325, 61]

# Result caching
result_cache_Size4 = [30, 579, 43, 606, 32]
result_cache_Size6 = [31, 526, 43, 557, 33]
result_cache_Size9 = [24, 498, 34, 528, 27]


color4 = 'tab:green'
color2 = 'tab:orange'
color3 = 'tab:red'
color1 = 'tab:blue'


FontSize = 32
ParamsFontSize = '24'

labels =  ["shasum" , "face-detect" , "qrcode", "face-blur", "BST"]

plotWidthInche = 18
plotHeightInche = 9


def plotResultCaching():
    print("Plot Result caching")
    fileName = "resultCaching.png"
    plt.rcParams['font.size'] = ParamsFontSize
    x = np.arange(len(labels))  
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, round_robin_result_caching, color = 'white', width = barWidth, edgecolor = 'black', capsize=7, 
    label='Round-Robin')
    rects2 = ax.bar(x + barWidth, CSD_result_caching, color = 'white', width = barWidth, edgecolor = 'black', capsize=7, label='CSD',
     hatch="||")
    rects3 = ax.bar(x + 2*barWidth, CCBS_result_caching, color = 'white', width = barWidth, edgecolor = 'black', capsize=7, 
    label='CCBS',hatch="\\\\")

    ax.set_ylabel('Average Execution Time (ms)', fontsize=FontSize)
    ax.set_xlabel('Functions Name', fontsize=FontSize)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=FontSize)
    ax.legend()
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	    label.set_fontsize(FontSize) 
    ax.legend()
  
    fig.set_size_inches(plotWidthInche, plotHeightInche)
    fig.tight_layout()
    fig.savefig(fileName, dpi=100, pad_inches=0)
    plt.show()


def plotResultCachingInController():
    print("Plot result caching RR - In Controller - CSD")
    fileName = "resultCachingInController.png"
    plt.rcParams['font.size'] = ParamsFontSize
    x = np.arange(len(labels))  # the label locations
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, round_robin_result_caching, color = 'white', width = barWidth, edgecolor = 'black', capsize=7, 
    label='Round-Robin')
    rects2 = ax.bar(x + barWidth, cacheInControllerSize4, color = 'white', width = barWidth, edgecolor = 'black', capsize=7,
     label='Cache In Controller', hatch="||")
    rects3 = ax.bar(x + 2*barWidth, CSD_result_caching, color = 'white', width = barWidth, edgecolor = 'black', capsize=7, 
    label='CSD',hatch="\\\\")

    ax.set_ylabel('Average Execution Time (ms)', fontsize=FontSize)
    ax.set_xlabel('Functions Name', fontsize=FontSize)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=FontSize)
    ax.legend()
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	    label.set_fontsize(FontSize) 
    ax.legend()
 
    fig.set_size_inches(plotWidthInche, plotHeightInche)
    fig.tight_layout()
    fig.savefig(fileName, dpi=100, pad_inches=0)
    plt.show()


    
def plotContentCaching():
    print("Plot Content caching")
    fileName = "ContentCaching.png"
    plt.rcParams['font.size'] = ParamsFontSize
    x = np.arange(len(labels)) 
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, round_robin_content_caching, color = 'white', width = barWidth, edgecolor = 'black', capsize=7, 
    label='Round-Robin')
    rects2 = ax.bar(x + barWidth, CSD_content_caching, color = 'white', width = barWidth, edgecolor = 'black', capsize=7, label='CSD',
     hatch="||")
    rects3 = ax.bar(x + 2*barWidth, CCBS_content_caching, color = 'white', width = barWidth, edgecolor = 'black', capsize=7, 
    label='CCBS',hatch="\\\\")

    ax.set_ylabel('Average Execution Time (ms)', fontsize=FontSize)
    ax.set_xlabel('Functions Name', fontsize=FontSize)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=FontSize)
    
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	    label.set_fontsize(FontSize) 
    ax.legend()

    fig.set_size_inches(plotWidthInche, plotHeightInche)
    fig.tight_layout()
    fig.savefig(fileName, dpi=100, pad_inches=0)

    plt.show()


def plotInControllerCachingInDifferentSizes():
    print("Plot In Controller caching in different sizes")
    fileName = "resultCachingInController_differentSizes.png"
    plt.rcParams['font.size'] = ParamsFontSize
    x = np.arange(len(labels))  # the label locations
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, cacheInControllerSize4, color = 'white', width = barWidth, edgecolor = 'black', capsize=7, 
    label='Size = 4')
    rects2 = ax.bar(x + barWidth, cacheInControllerSize8, color = 'white', width = barWidth, edgecolor = 'black', capsize=7, 
    label='Size = 8', hatch="||")

    ax.set_ylabel('Average Execution Time (ms)', fontsize=FontSize)
    ax.set_xlabel('Functions Name', fontsize=FontSize)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=FontSize)
    ax.legend()
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	    label.set_fontsize(FontSize) 
    ax.legend()

    fig.set_size_inches(plotWidthInche, plotHeightInche)
    fig.tight_layout()
    fig.savefig(fileName, dpi=100, pad_inches=0)
    plt.show()



def plotResultCachingInDifferentSizes():
    print("Plot Result caching in different sizes")
    fileName = "resultCaching_differentSizes.png"
    plt.rcParams['font.size'] = ParamsFontSize
    x = np.arange(len(labels)) 
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, result_cache_Size4, color = 'white', width = barWidth, edgecolor = 'black', capsize=7, 
    label='Size = 4')
    rects2 = ax.bar(x + barWidth, result_cache_Size6, color = 'white', width = barWidth, edgecolor = 'black', capsize=7, 
    label='Size = 6', hatch="||")
    rects3 = ax.bar(x + 2*barWidth, result_cache_Size9, color = 'white', width = barWidth, edgecolor = 'black', capsize=7, 
    label='Size = 9', hatch="\\\\")

    ax.set_ylabel('Average Execution Time (ms)', fontsize=FontSize)
    ax.set_xlabel('Functions Name', fontsize=FontSize)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=FontSize)
    ax.legend()
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	    label.set_fontsize(FontSize) 
    ax.legend()
  
    fig.set_size_inches(plotWidthInche, plotHeightInche)
    fig.tight_layout()
    fig.savefig(fileName, dpi=100, pad_inches=0)
    plt.show()

 

def plotResultCachingTAHCandFoCInDifferentSizes():
    print("Plot TAHCandFoC  Result caching in different sizes")
    fileName = "TAHCandFoC_resultCaching_differentSizes.png"
    barWidth = 0.22
    plt.rcParams['font.size'] = ParamsFontSize
    x = np.arange(len(labels))  
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - 1.5*barWidth, cacheInControllerSize5, color = 'white', width = barWidth, edgecolor = color1, capsize=7, 
    label='FoC Size = 5')
    rects2 = ax.bar(x - 0.5*barWidth, cacheInControllerSize10, color = 'white', width = barWidth, edgecolor = color2, capsize=7, 
    label='FoC Size = 10', hatch="||")
    rects3 = ax.bar(x + 0.5*barWidth, cacheSchedulerSize5, color = 'white', width = barWidth, edgecolor = color3, capsize=7, 
    label='TAHC Size = 5', hatch="\\\\")
    rects4 = ax.bar(x + 1.5*barWidth, cacheInControllerSize10, color = 'white', width = barWidth, edgecolor = color4, capsize=7, 
    label='TAHC Size = 10', hatch="-")

    ax.set_ylabel('Average Execution Time (ms)', fontsize=FontSize)
    ax.set_xlabel('Functions Name', fontsize=FontSize)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=FontSize)
    ax.legend()
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	    label.set_fontsize(FontSize) 
    ax.legend()
 
    fig.set_size_inches(plotWidthInche, plotHeightInche)
    fig.tight_layout()
    fig.savefig(fileName, dpi=100, pad_inches=0)
    plt.show()


def plotResultCachingTAHCInDifferentSizes():
    print("Plot TAHC  Result caching in different sizes")
    fileName = "TAHC_resultCaching_differentSizes.png"
    barWidth = 0.15
    plt.rcParams['font.size'] = ParamsFontSize
    x = np.arange(len(labels)) 
    fig, ax = plt.subplots()

    rects3 = ax.bar(x - 0.5*barWidth, cacheSchedulerSize5, color = 'white', width = barWidth, edgecolor = color1, capsize=7, 
    label='TAHC Size = 5', hatch="")
    rects4 = ax.bar(x + 0.5*barWidth, cacheInControllerSize10, color = 'white', width = barWidth, edgecolor = color2, capsize=7, 
    label='TAHC Size = 10', hatch="\\\\")

    ax.set_ylabel('Average Execution Time (ms)', fontsize=FontSize)
    ax.set_xlabel('Functions Name', fontsize=FontSize)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=FontSize)
    ax.legend()
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	    label.set_fontsize(FontSize) 
    ax.legend()
    
    fig.set_size_inches(plotWidthInche, plotHeightInche)
    fig.tight_layout()
    fig.savefig(fileName, dpi=100, pad_inches=0)
    plt.show()    


def plotResultCachingFoCInDifferentSizes():
    print("Plot FoC  Result caching in different sizes")
    fileName = "FoC_resultCaching_differentSizes.png"
    barWidth = 0.15
    plt.rcParams['font.size'] = ParamsFontSize
    x = np.arange(len(labels)) 
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - 0.5*barWidth, cacheInControllerSize5, color = 'white', width = barWidth, edgecolor = color1, capsize=7, 
    label='FoC Size = 5')
    rects2 = ax.bar(x + 0.5*barWidth, cacheInControllerSize10, color = 'white', width = barWidth, edgecolor = color2, capsize=7, 
    label='FoC Size = 10', hatch="||")

    ax.set_ylabel('Average Execution Time (ms)', fontsize=FontSize)
    ax.set_xlabel('Functions Name', fontsize=FontSize)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=FontSize)
    ax.legend()
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	    label.set_fontsize(FontSize) 
    ax.legend()
  
    fig.set_size_inches(plotWidthInche, plotHeightInche)
    fig.tight_layout()
    fig.savefig(fileName, dpi=100, pad_inches=0)
    plt.show()


def plotResultCachingTypicalFoCTAHC():
    print("Plot Result caching in Typical FoC TAHC")
    fileName = "resultCaching_TypicalFoCTAH_cacheSize5.png"
    plt.rcParams['font.size'] = ParamsFontSize
    x = np.arange(len(labels))  
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - barWidth, round_robin_result_caching, color = 'white', width = barWidth, edgecolor = color1, capsize=7, 
    label='Typical')
    rects2 = ax.bar(x, cacheInControllerSize5, color = 'white', width = barWidth, edgecolor = color2, capsize=7, 
    label='FoC', hatch="||")
    rects3 = ax.bar(x + barWidth, cacheSchedulerSize5, color = 'white', width = barWidth, edgecolor = color3, capsize=7, 
    label='TAHC', hatch="\\\\")

    ax.set_ylabel('Average Execution Time (ms)', fontsize=FontSize)
    ax.set_xlabel('Functions Name', fontsize=FontSize)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=FontSize)
    ax.legend()
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	    label.set_fontsize(FontSize) 
    ax.legend()
  
    fig.set_size_inches(plotWidthInche, plotHeightInche)
    fig.tight_layout()
    fig.savefig(fileName, dpi=100, pad_inches=0)
    plt.show()
 

def plotResultCachingTypicalTAHCBatch():
    print("Plot Result caching in Typical TAHC Batch")
    fileName = "resultCaching_TypicalTAHBatch_cacheSize5.png"
    plt.rcParams['font.size'] = ParamsFontSize
    x = np.arange(len(labels))
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - barWidth, round_robin_result_caching, color = 'white', width = barWidth, edgecolor = color1, capsize=7, 
    label='Typical')
    rects2 = ax.bar(x , cacheSchedulerSize5, color = 'white', width = barWidth, edgecolor = color2, capsize=7, 
    label='TAHC', hatch="||")
    rects3 = ax.bar(x + barWidth, batchIncacheSchedulerSize5, color = 'white', width = barWidth, edgecolor = color3, capsize=7, 
    label='B-TAHC', hatch="\\\\")

    ax.set_ylabel('Average Execution Time (ms)', fontsize=FontSize)
    ax.set_xlabel('Functions Name', fontsize=FontSize)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=FontSize)
    ax.legend()
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
	    label.set_fontsize(FontSize) 
    ax.legend()
    
    fig.set_size_inches(plotWidthInche, plotHeightInche)
    fig.tight_layout()
    fig.savefig(fileName, dpi=100, pad_inches=0)
    plt.show()


# plotResultCaching()
# plotResultCachingInController()
# plotContentCaching()
# plotInControllerCachingInDifferentSizes()
# plotResultCachingInDifferentSizes()

plotResultCachingTAHCInDifferentSizes()
plotResultCachingFoCInDifferentSizes()
plotResultCachingTAHCandFoCInDifferentSizes()
plotResultCachingTypicalFoCTAHC()
plotResultCachingTypicalTAHCBatch()

