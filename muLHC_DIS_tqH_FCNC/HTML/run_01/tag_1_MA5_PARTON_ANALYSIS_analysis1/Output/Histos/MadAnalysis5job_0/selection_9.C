void selection_9()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo19","canvas_plotflow_tempo19",0,0,700,500);
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
  TH1F* S10_PT_0 = new TH1F("S10_PT_0","S10_PT_0",40,0.0,500.0);
  // Content
  S10_PT_0->SetBinContent(0,0.0); // underflow
  S10_PT_0->SetBinContent(1,0.010424838274429235);
  S10_PT_0->SetBinContent(2,0.02779955539848017);
  S10_PT_0->SetBinContent(3,0.04403100271177077);
  S10_PT_0->SetBinContent(4,0.05611058071229931);
  S10_PT_0->SetBinContent(5,0.06435416934777977);
  S10_PT_0->SetBinContent(6,0.06921306854351075);
  S10_PT_0->SetBinContent(7,0.07256767798823921);
  S10_PT_0->SetBinContent(8,0.07309417790109035);
  S10_PT_0->SetBinContent(9,0.06775389878503973);
  S10_PT_0->SetBinContent(10,0.06695661891700944);
  S10_PT_0->SetBinContent(11,0.062248139696380204);
  S10_PT_0->SetBinContent(12,0.05629109068242041);
  S10_PT_0->SetBinContent(13,0.05435054100362978);
  S10_PT_0->SetBinContent(14,0.05185339141697033);
  S10_PT_0->SetBinContent(15,0.04729535217143951);
  S10_PT_0->SetBinContent(16,0.04448230263706938);
  S10_PT_0->SetBinContent(17,0.03974373342142078);
  S10_PT_0->SetBinContent(18,0.03921723350856964);
  S10_PT_0->SetBinContent(19,0.03523082416841983);
  S10_PT_0->SetBinContent(20,0.03405746436264014);
  S10_PT_0->SetBinContent(21,0.03219212467140039);
  S10_PT_0->SetBinContent(22,0.029785235069800655);
  S10_PT_0->SetBinContent(23,0.02734826547317991);
  S10_PT_0->SetBinContent(24,0.02546788578442965);
  S10_PT_0->SetBinContent(25,0.024550255936320275);
  S10_PT_0->SetBinContent(26,0.023000826192789547);
  S10_PT_0->SetBinContent(27,0.021541646434320195);
  S10_PT_0->SetBinContent(28,0.02100009652396021);
  S10_PT_0->SetBinContent(29,0.01901441685263973);
  S10_PT_0->SetBinContent(30,0.018713556902439556);
  S10_PT_0->SetBinContent(31,0.016652657243569853);
  S10_PT_0->SetBinContent(32,0.015674857405420115);
  S10_PT_0->SetBinContent(33,0.014787317552330101);
  S10_PT_0->SetBinContent(34,0.014396197617070205);
  S10_PT_0->SetBinContent(35,0.012921977861090346);
  S10_PT_0->SetBinContent(36,0.011432718107599984);
  S10_PT_0->SetBinContent(37,0.011327418125029758);
  S10_PT_0->SetBinContent(38,0.01080090821218028);
  S10_PT_0->SetBinContent(39,0.009913370359089933);
  S10_PT_0->SetBinContent(40,0.008709925558290066);
  S10_PT_0->SetBinContent(41,0.11799768046844063); // overflow
  S10_PT_0->SetEntries(100000);
  // Style
  S10_PT_0->SetLineColor(9);
  S10_PT_0->SetLineStyle(1);
  S10_PT_0->SetLineWidth(1);
  S10_PT_0->SetFillColor(9);
  S10_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_20","mystack");
  stack->Add(S10_PT_0);
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
  stack->GetXaxis()->SetTitle("p_{T} [ h_{1} ] (GeV/c) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_9.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_9.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_9.eps");

}
