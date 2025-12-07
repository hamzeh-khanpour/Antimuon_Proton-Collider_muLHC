def selection_12():

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

    # Creating weights for histo: y13_M_0
    y13_M_0_weights = numpy.array([0.0030086105379999173,0.012320258108109976,0.018924157094019973,0.025076766149229723,0.030010885391549905,0.03226734504504957,0.03508039461307969,0.036735124358980575,0.03873585405174996,0.03870576405637055,0.03718642428967928,0.037532414236549315,0.035937844481410304,0.03581750449988963,0.03479457465697,0.03465918467776039,0.03363626483483923,0.03232751503580991,0.030206445361519854,0.03156031515362057,0.02967993544237034,0.028852565569420667,0.02751373577501041,0.026475765934400316,0.02649081593208925,0.025618316066069707,0.025407716098409288,0.022715006511899845,0.022985776470320605,0.022970736472630135,0.022549536537309296,0.019856826950799857,0.019841786953109387,0.01844277716794033,0.01920997705012966,0.017795927267270136,0.0166676974405203,0.017209247357360284,0.016201367512129593,0.01579520757449922])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y13_M_0_weights,\
             label="$run\_01$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$M$ $[ mu+_{1} p_{1} ]$ $(GeV/c^{2})$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y13_M_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y13_M_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_12.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_12.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_12.eps')

# Running!
if __name__ == '__main__':
    selection_12()
