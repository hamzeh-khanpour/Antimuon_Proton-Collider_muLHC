def selection_8():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(-10.0,10.0,41,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([-9.75,-9.25,-8.75,-8.25,-7.75,-7.25,-6.75,-6.25,-5.75,-5.25,-4.75,-4.25,-3.75,-3.25,-2.75,-2.25,-1.75,-1.25,-0.75,-0.25,0.25,0.75,1.25,1.75,2.25,2.75,3.25,3.75,4.25,4.75,5.25,5.75,6.25,6.75,7.25,7.75,8.25,8.75,9.25,9.75])

    # Creating weights for histo: y9_ETA_0
    y9_ETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,3.008610500659917e-05,0.0001203443800264033,0.00036103324007919337,0.0007521524751650041,0.0027227925480972173,0.0062579089613727735,0.015930587355995132,0.034839704217642736,0.06626463900203589,0.10617388237828551,0.1477377754799124,0.19771076718587838,0.23886856035490578,0.23766516055463444,0.18671436901095423,0.12872337863573813,0.07119875818311848,0.0357573340653434,0.015238607470843261,0.00714544881406749,0.002587404570567605,0.0009025830501979916,0.00034599014257590124,0.00015043047503300415,7.521524751650041e-05,1.5043047503300413e-05,1.5043047503300413e-05,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y9_ETA_0_weights,\
             label="$run\_01$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$\eta$ $[ t_{1} ]$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y9_ETA_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y9_ETA_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_8.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_8.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_8.eps')

# Running!
if __name__ == '__main__':
    selection_8()
