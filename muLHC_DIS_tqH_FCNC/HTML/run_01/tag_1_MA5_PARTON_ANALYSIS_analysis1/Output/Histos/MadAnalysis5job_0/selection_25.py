def selection_25():

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

    # Creating weights for histo: y26_DELTAR_0
    y26_DELTAR_0_weights = numpy.array([0.009116088720188539,0.03071790568750053,0.049401373064520825,0.06665576064217023,0.07753187911526746,0.08727977774675595,0.0988328461248159,0.10700118497805944,0.12007358314282006,0.13313098130968654,0.145240679609601,0.15935107762863637,0.14697057936673963,0.08425612817124736,0.05239494264425235,0.03893141453440263,0.028025206065529742,0.020112557176389788,0.014140468014813853,0.011282288416074869,0.007220663986288,0.0052048952692826025,0.003971365442458364,0.0026927056219699453,0.0018653387381243238,0.0009777982627264979,0.0007972816880692944,0.0004512915366429947,0.0002858179598738985,0.0001353874809928956,6.017220155239976e-05,6.017220155239976e-05,6.017220155239976e-05,1.5043047888100291e-05,3.008610577619918e-05,0.0,1.5043047888100291e-05,1.5043047888100291e-05,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y26_DELTAR_0_weights,\
             label="$run\_01$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$\Delta R$ $[ p_{1}, h_{1} ]$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y26_DELTAR_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y26_DELTAR_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_25.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_25.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_25.eps')

# Running!
if __name__ == '__main__':
    selection_25()
