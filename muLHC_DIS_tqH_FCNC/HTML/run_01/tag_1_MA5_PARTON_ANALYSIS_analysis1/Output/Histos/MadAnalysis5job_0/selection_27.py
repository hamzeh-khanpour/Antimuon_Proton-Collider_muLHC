def selection_27():

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

    # Creating weights for histo: y28_DELTAR_0
    y28_DELTAR_0_weights = numpy.array([0.009612509161405259,0.02462547528985943,0.03274872373611715,0.0378483127607134,0.04224088192054207,0.047490910916363496,0.054380619598561664,0.0633161978894442,0.07510994563364166,0.09341734213196667,0.12970117519191976,0.2084816601234935,0.3264642375568418,0.14077287307422445,0.07500464565378251,0.04864922069481237,0.029830364294314834,0.020157686144418163,0.013192757476607397,0.010139018060699346,0.00657381274261992,0.004573087125300814,0.0028581794533130084,0.0024369745338773167,0.0014290897266565042,0.0010379708014662326,0.0007671955532576992,0.0004813776079263984,0.0002707748482086099,0.00016547356834969645,0.00015043047122700548,9.025830273619946e-05,9.025830273619946e-05,7.521524561350083e-05,3.0086104245399184e-05,3.0086104245399184e-05,3.0086104245399184e-05,1.5043047122700547e-05,0.0,1.5043047122700547e-05])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y28_DELTAR_0_weights,\
             label="$run\_01$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$\Delta R$ $[ t_{1}, h_{1} ]$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y28_DELTAR_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y28_DELTAR_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_27.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_27.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_27.eps')

# Running!
if __name__ == '__main__':
    selection_27()
