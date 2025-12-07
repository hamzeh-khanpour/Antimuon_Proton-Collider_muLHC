def selection_23():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,10.0,41,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([0.125,0.375,0.625,0.875,1.125,1.375,1.625,1.875,2.125,2.375,2.625,2.875,3.125,3.375,3.625,3.875,4.125,4.375,4.625,4.875,5.125,5.375,5.625,5.875,6.125,6.375,6.625,6.875,7.125,7.375,7.625,7.875,8.125,8.375,8.625,8.875,9.125,9.375,9.625,9.875])

    # Creating weights for histo: y24_DELTAR_0
    y24_DELTAR_0_weights = numpy.array([0.0017600367237630202,0.005189852185455011,0.00947712151257,0.01313257793884774,0.01934536696375327,0.026641245818668335,0.03347078474677524,0.04544505286741919,0.05582476123832859,0.0686113492314793,0.08246599705699849,0.09431992519652975,0.102969683838954,0.09740375471252408,0.09404914523902855,0.08795671619523257,0.08293233698380664,0.07620808803917452,0.06931837912051127,0.06214284024670891,0.05605040120291449,0.05110124197968283,0.04445221302324496,0.03814917401250413,0.034418494598032603,0.029484375372440415,0.02588908593671949,0.021225746668628514,0.017464977258879598,0.014260807761772572,0.011583148182030052,0.008649753642425019,0.006664070954077032,0.00528011017128906,0.0034899874522480237,0.002632533586825026,0.002030811681265011,0.0013689177851489633,0.0008574538654229978,0.00045129152916999546])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y24_DELTAR_0_weights,\
             label="$run\_01$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$\Delta R$ $[ mu+_{1}, p_{1} ]$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y24_DELTAR_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y24_DELTAR_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_23.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_23.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_23.eps')

# Running!
if __name__ == '__main__':
    selection_23()
