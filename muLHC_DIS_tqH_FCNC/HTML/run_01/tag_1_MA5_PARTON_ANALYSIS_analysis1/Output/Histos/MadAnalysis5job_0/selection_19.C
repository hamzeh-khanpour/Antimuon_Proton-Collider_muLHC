void selection_19()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo39","canvas_plotflow_tempo39",0,0,700,500);
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
  TH1F* S20_M_0 = new TH1F("S20_M_0","S20_M_0",40,0.0,500.0);
  // Content
  S20_M_0->SetBinContent(0,0.0); // underflow
  S20_M_0->SetBinContent(1,0.0);
  S20_M_0->SetBinContent(2,0.0);
  S20_M_0->SetBinContent(3,0.0);
  S20_M_0->SetBinContent(4,0.0);
  S20_M_0->SetBinContent(5,0.0);
  S20_M_0->SetBinContent(6,0.0);
  S20_M_0->SetBinContent(7,0.0);
  S20_M_0->SetBinContent(8,0.0);
  S20_M_0->SetBinContent(9,0.0);
  S20_M_0->SetBinContent(10,0.0);
  S20_M_0->SetBinContent(11,0.0);
  S20_M_0->SetBinContent(12,0.0);
  S20_M_0->SetBinContent(13,0.0);
  S20_M_0->SetBinContent(14,0.0034147726072899704);
  S20_M_0->SetBinContent(15,0.10877628749037081);
  S20_M_0->SetBinContent(16,0.12559438555623445);
  S20_M_0->SetBinContent(17,0.11103278723086595);
  S20_M_0->SetBinContent(18,0.09743383879478955);
  S20_M_0->SetBinContent(19,0.08463220026701988);
  S20_M_0->SetBinContent(20,0.07307914159565947);
  S20_M_0->SetBinContent(21,0.06439930259386936);
  S20_M_0->SetBinContent(22,0.05753967338274918);
  S20_M_0->SetBinContent(23,0.0499579742546694);
  S20_M_0->SetBinContent(24,0.04379032496396926);
  S20_M_0->SetBinContent(25,0.03838986558503977);
  S20_M_0->SetBinContent(26,0.035366215932769375);
  S20_M_0->SetBinContent(27,0.030883386448309447);
  S20_M_0->SetBinContent(28,0.027799556802959955);
  S20_M_0->SetBinContent(29,0.02539266707976015);
  S20_M_0->SetBinContent(30,0.02253448740846017);
  S20_M_0->SetBinContent(31,0.021556687520910358);
  S20_M_0->SetBinContent(32,0.019164847795979757);
  S20_M_0->SetBinContent(33,0.01699864804509982);
  S20_M_0->SetBinContent(34,0.016622568088350248);
  S20_M_0->SetBinContent(35,0.015328868237129966);
  S20_M_0->SetBinContent(36,0.014245768361689998);
  S20_M_0->SetBinContent(37,0.013102498493169776);
  S20_M_0->SetBinContent(38,0.012801638527769657);
  S20_M_0->SetBinContent(39,0.011161938716340502);
  S20_M_0->SetBinContent(40,0.010906208745750287);
  S20_M_0->SetBinContent(41,0.35239845947302345); // overflow
  S20_M_0->SetEntries(100000);
  // Style
  S20_M_0->SetLineColor(9);
  S20_M_0->SetLineStyle(1);
  S20_M_0->SetLineWidth(1);
  S20_M_0->SetFillColor(9);
  S20_M_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_40","mystack");
  stack->Add(S20_M_0);
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
  stack->GetXaxis()->SetTitle("M [ p_{1} t_{1} ] (GeV/c^{2}) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_19.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_19.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_19.eps");

}
