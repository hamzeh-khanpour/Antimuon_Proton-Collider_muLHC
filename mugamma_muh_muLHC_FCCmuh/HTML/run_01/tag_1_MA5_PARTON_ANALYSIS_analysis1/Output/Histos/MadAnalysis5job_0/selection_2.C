void selection_2()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo5","canvas_plotflow_tempo5",0,0,700,500);
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
  TH1F* S3_SQRTS_0 = new TH1F("S3_SQRTS_0","S3_SQRTS_0",40,0.0,500.0);
  // Content
  S3_SQRTS_0->SetBinContent(0,0.0); // underflow
  S3_SQRTS_0->SetBinContent(1,0.0);
  S3_SQRTS_0->SetBinContent(2,0.0);
  S3_SQRTS_0->SetBinContent(3,0.0);
  S3_SQRTS_0->SetBinContent(4,0.0);
  S3_SQRTS_0->SetBinContent(5,0.0);
  S3_SQRTS_0->SetBinContent(6,0.0);
  S3_SQRTS_0->SetBinContent(7,0.0);
  S3_SQRTS_0->SetBinContent(8,0.0);
  S3_SQRTS_0->SetBinContent(9,0.0);
  S3_SQRTS_0->SetBinContent(10,0.0);
  S3_SQRTS_0->SetBinContent(11,0.00032237907467299833);
  S3_SQRTS_0->SetBinContent(12,0.0006372125499388);
  S3_SQRTS_0->SetBinContent(13,0.0005015376605977987);
  S3_SQRTS_0->SetBinContent(14,0.00039014396934919864);
  S3_SQRTS_0->SetBinContent(15,0.00032160517473379805);
  S3_SQRTS_0->SetBinContent(16,0.0002674802789860012);
  S3_SQRTS_0->SetBinContent(17,0.000231106881843597);
  S3_SQRTS_0->SetBinContent(18,0.00020735768370940046);
  S3_SQRTS_0->SetBinContent(19,0.00018128678575760312);
  S3_SQRTS_0->SetBinContent(20,0.0001608267873649978);
  S3_SQRTS_0->SetBinContent(21,0.00014525198858859754);
  S3_SQRTS_0->SetBinContent(22,0.00012924178984640355);
  S3_SQRTS_0->SetBinContent(23,0.00011289309113080302);
  S3_SQRTS_0->SetBinContent(24,0.00010389649183760104);
  S3_SQRTS_0->SetBinContent(25,9.27716427116003e-05);
  S3_SQRTS_0->SetBinContent(26,8.425870338040061e-05);
  S3_SQRTS_0->SetBinContent(27,7.598761403020052e-05);
  S3_SQRTS_0->SetBinContent(28,6.650730477500014e-05);
  S3_SQRTS_0->SetBinContent(29,6.302473504860056e-05);
  S3_SQRTS_0->SetBinContent(30,5.610797559200052e-05);
  S3_SQRTS_0->SetBinContent(31,5.209335590740027e-05);
  S3_SQRTS_0->SetBinContent(32,4.865916617719982e-05);
  S3_SQRTS_0->SetBinContent(33,4.2080986694e-05);
  S3_SQRTS_0->SetBinContent(34,3.8985376937199756e-05);
  S3_SQRTS_0->SetBinContent(35,3.632507714620035e-05);
  S3_SQRTS_0->SetBinContent(36,3.298762740839973e-05);
  S3_SQRTS_0->SetBinContent(37,3.0182227628799785e-05);
  S3_SQRTS_0->SetBinContent(38,2.8731157742799894e-05);
  S3_SQRTS_0->SetBinContent(39,2.6893137887199876e-05);
  S3_SQRTS_0->SetBinContent(40,2.1766028289999945e-05);
  S3_SQRTS_0->SetBinContent(41,0.0003273126742854009); // overflow
  S3_SQRTS_0->SetEntries(100000);
  // Style
  S3_SQRTS_0->SetLineColor(9);
  S3_SQRTS_0->SetLineStyle(1);
  S3_SQRTS_0->SetLineWidth(1);
  S3_SQRTS_0->SetFillColor(9);
  S3_SQRTS_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_6","mystack");
  stack->Add(S3_SQRTS_0);
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
  stack->GetXaxis()->SetTitle("#sqrt{#hat{s}} (GeV) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(1);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_2.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_2.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_2.eps");

}
