def selection_22():

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

    # Creating weights for histo: y23_DELTAR_0
    y23_DELTAR_0_weights = numpy.array([0.001579520693819914,0.004197011186435954,0.007536567539084098,0.011522977766343714,0.015464257002351687,0.021361125859280995,0.028882654401280305,0.03879602247963666,0.05030396024889579,0.06585846723375309,0.09036360248358777,0.1239697759692438,0.1460379716914638,0.12351847605672543,0.10782857909811264,0.09811077098184821,0.0878514129705598,0.07941225460643722,0.06892725663888769,0.060909308193116234,0.050710120170164255,0.04362484154360066,0.03781822266917697,0.030808164028032457,0.026220034917412236,0.02059393600799589,0.016366836827392303,0.013704217343524233,0.009401906177500013,0.006889716664472045,0.0050995940114759875,0.0036705042884959825,0.0027679214634559485,0.001368917734643964,0.0012335297608880656,0.0006919802658640065,0.00028581794459600103,0.00022564575625999873,0.00015043047084000564,0.00010530137958799424])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y23_DELTAR_0_weights,\
             label="$run\_01$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$\Delta R$ $[ mu+_{1}, h_{1} ]$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y23_DELTAR_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y23_DELTAR_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_22.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_22.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_22.eps')

# Running!
if __name__ == '__main__':
    selection_22()
