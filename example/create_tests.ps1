# This script simply creates all of the .pdf files using the
# various templates from the sample ipynb.

$templates = @("classic","classicm")
$notebook = "test"

foreach ($template in $templates){
	jupyter nbconvert --to pdf ($notebook+".ipynb") --template $template
	if ($template -eq "article") {$template = "default"}
	$NewName = $notebook+"_"+$template+"_template.pdf"
	Move-Item -path ($notebook+".pdf") -destination $NewName -force
}
