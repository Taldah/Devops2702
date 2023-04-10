properties([pipelineTriggers([githubPush()])])node{
    stage("clone"){
        git "https://github.com/avielb/DevOps2702.git"
    }
    stage("execute"){
        sh "ls -l"
        sh "python disk_resizer.py"
 }
}
