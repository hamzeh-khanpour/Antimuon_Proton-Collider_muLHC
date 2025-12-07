void selection_11()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo23","canvas_plotflow_tempo23",0,0,700,500);
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  canvas->SetHighLightColor(2);
  canvas->SetFillColor(0);
  canvas->SetBorderMode(0);
  canvas->SetBorderSize(3);
  canvas->SetFrameBorderMode(0);
  canvas->SetFrameBorderSize(0);
  canvas->SetTickx(1);
  canvas->SetTicky(1);
  canvas->SetLeftMargin(0.14);
  canvas->SetRightMargin(0.05);
  canvas->SetBottomMargin(0.15);
  canvas->SetTopMargin(0.05);

  // Creating a new TH1F
  TH1F* S12_M_0 = new TH1F("S12_M_0","S12_M_0",40,0.0,500.0);
  // Content
  S12_M_0->SetBinContent(0,0.0); // underflow
  S12_M_0->SetBinContent(1,0.0);
  S12_M_0->SetBinContent(2,0.0);
  S12_M_0->SetBinContent(3,0.0);
  S12_M_0->SetBinContent(4,0.0);
  S12_M_0->SetBinContent(5,0.0);
  S12_M_0->SetBinContent(6,0.0);
  S12_M_0->SetBinContent(7,0.0);
  S12_M_0->SetBinContent(8,0.0);
  S12_M_0->SetBinContent(9,0.0);
  S12_M_0->SetBinContent(10,0.0);
  S12_M_0->SetBinContent(11,0.0036554613633399628);
  S12_M_0->SetBinContent(12,0.011959227917099446);
  S12_M_0->SetBinContent(13,0.015373997322359957);
  S12_M_0->SetBinContent(14,0.017690626918879977);
  S12_M_0->SetBinContent(15,0.02062402640797915);
  S12_M_0->SetBinContent(16,0.023271595946860416);
  S12_M_0->SetBinContent(17,0.023376895928520654);
  S12_M_0->SetBinContent(18,0.02265483605427952);
  S12_M_0->SetBinContent(19,0.02488120566651983);
  S12_M_0->SetBinContent(20,0.02545283556696087);
  S12_M_0->SetBinContent(21,0.02620499543595959);
  S12_M_0->SetBinContent(22,0.02545283556696087);
  S12_M_0->SetBinContent(23,0.025362585582679426);
  S12_M_0->SetBinContent(24,0.02543779556958034);
  S12_M_0->SetBinContent(25,0.026671325354740393);
  S12_M_0->SetBinContent(26,0.024339655760839844);
  S12_M_0->SetBinContent(27,0.02611473545167988);
  S12_M_0->SetBinContent(28,0.024715735695339205);
  S12_M_0->SetBinContent(29,0.024490085734639937);
  S12_M_0->SetBinContent(30,0.024429915745119553);
  S12_M_0->SetBinContent(31,0.022098236151220745);
  S12_M_0->SetBinContent(32,0.0247608556874808);
  S12_M_0->SetBinContent(33,0.0219026761852808);
  S12_M_0->SetBinContent(34,0.0233317659363808);
  S12_M_0->SetBinContent(35,0.022384056101440397);
  S12_M_0->SetBinContent(36,0.020819576373920835);
  S12_M_0->SetBinContent(37,0.02142130626911946);
  S12_M_0->SetBinContent(38,0.02125582629794058);
  S12_M_0->SetBinContent(39,0.01994708652587961);
  S12_M_0->SetBinContent(40,0.01984178654421937);
  S12_M_0->SetBinContent(41,0.8443814529367776); // overflow
  S12_M_0->SetEntries(100000);
  // Style
  S12_M_0->SetLineColor(9);
  S12_M_0->SetLineStyle(1);
  S12_M_0->SetLineWidth(1);
  S12_M_0->SetFillColor(9);
  S12_M_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_24","mystack");
  stack->Add(S12_M_0);
  stack->Draw("");

  // Y axis
  stack->GetYaxis()->SetLabelSize(0.04);
  stack->GetYaxis()->SetLabelOffset(0.005);
  stack->GetYaxis()->SetTitleSize(0.06);
  stack->GetYaxis()->SetTitleFont(22);
  stack->GetYaxis()->SetTitleOffset(1);
  stack->GetYaxis()->SetTitle("Events  ( L_{int} = 10 fb^{-1} )");

  // X axis
  stack->GetXaxis()->SetLabelSize(0.04);
  stack->GetXaxis()->SetLabelOffset(0.005);
  stack->GetXaxis()->SetTitleSize(0.06);
  stack->GetXaxis()->SetTitleFont(22);
  stack->GetXaxis()->SetTitleOffset(1);
  stack->GetXaxis()->SetTitle("M [ h_{1} mu+_{1} ] (GeV/c^{2}) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_11.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_11.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_11.eps");

}
