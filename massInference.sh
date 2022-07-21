#! /bin/bash
$#
if [ "$#" != "3" ]; then
	echo "Error: You must provide 3 Arguments. (Path to detect.py, path to image/folder, version of yolo" 
fi

echo $1 $2 $3
commandPath=$1
folderPath=$2
versionOfYolo=$3
projectPath=/tmp/detectResults
name='run'
#python3 /home/limar/yuvi/practice-repository2/yolov5/detect.py --weights yolov5x6.pt --source  /home/limar/yuvi/practice-repository/cam_000/ --save-txt --project /tmp/yuvi --name run --exist-ok

rm -rf $projectPath
python3 $commandPath --weights $versionOfYolo --source  $folderPath --save-txt --project $projectPath --name $name --exist-ok
# because of --project --name and --exist-ok, the results will always be in $projectPath/$name/labels

resultsPath=$projectPath/$name/"labels"
echo "looking for results in $resultsPath"

for f in $resultsPath/*.txt 
do 
	echo $f >> $resultsPath/'results.text'
       	cat $f >> $resultsPath/'results.text'
       	echo "" >> $resultsPath/'results.text'
done
