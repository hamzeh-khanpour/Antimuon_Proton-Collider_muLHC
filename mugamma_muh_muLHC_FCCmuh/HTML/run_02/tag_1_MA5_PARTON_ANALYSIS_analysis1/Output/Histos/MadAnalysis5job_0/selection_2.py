def selection_2():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,500.0,41,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([6.25,18.75,31.25,43.75,56.25,68.75,81.25,93.75,106.25,118.75,131.25,143.75,156.25,168.75,181.25,193.75,206.25,218.75,231.25,243.75,256.25,268.75,281.25,293.75,306.25,318.75,331.25,343.75,356.25,368.75,381.25,393.75,406.25,418.75,431.25,443.75,456.25,468.75,481.25,493.75])

    # Creating weights for histo: y3_SQRTS_0
    y3_SQRTS_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0004464524030764998,0.0008824565060810003,0.0006988109048155001,0.0005487599037815,0.00045820690315749997,0.0003791182026125004,0.0003334789022980003,0.00029553080203650027,0.00026614460183400023,0.00023240490160150024,0.00021288660146699982,0.000193876301336,0.0001706576011760001,0.00016340170112599976,0.00013771600094899982,0.0001315486009065003,0.00012523600086300024,0.00010912800075200015,9.889723068149998e-05,8.648973059600002e-05,8.235390056750004e-05,7.567851052149998e-05,7.306641050350003e-05,7.270362050100004e-05,5.775656039799998e-05,5.630539038799997e-05,5.013792034549999e-05,4.455092030700002e-05,4.3462540299500003e-05,4.157602028650001e-05])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y3_SQRTS_0_weights,\
             label="$run\_02$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$\sqrt{\hat{s}}$ $(GeV)$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y3_SQRTS_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y3_SQRTS_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_2.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_2.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_2.eps')

# Running!
if __name__ == '__main__':
    selection_2()
