import argparse
import xml.etree.ElementTree as et
from xml.etree import ElementTree

import jenkins

parser = argparse.ArgumentParser(description='Creates Jenkins job that runs unit tests each time it detects a commit.')
parser.add_argument('--project-path', type=str, default='/home/lale/2020_01_Jenkins')
parser.add_argument('--branch', type=str, default='main')
parser.add_argument('--jenkins-address', type=str, default='http://localhost:8080')
parser.add_argument('--jenkins-user', type=str, default='admin')
parser.add_argument('--jenkins-pw', type=str, default='485971c4c0924147869c52e08ed99265')
parser.add_argument('--job-name', type=str, default='unit_tests')

if __name__ == '__main__':
    args = parser.parse_args()

    server = jenkins.Jenkins(args.jenkins_address, username=args.jenkins_user, password=args.jenkins_pw)
    if server.get_job_name(args.job_name):
        print('Job already exists!')
        exit(1)

    try:
        tree = et.parse('config.xml')
    except FileNotFoundError:
        print('Config XML not present!')
        exit(1)

    root = tree.getroot()

    url_node = tree.find('./scm/userRemoteConfigs/hudson.plugins.git.UserRemoteConfig/url')
    url_node.text = args.project_path

    branch_node = tree.find('./scm/branches/hudson.plugins.git.BranchSpec/name')
    branch_node.text = f'*/{args.branch}'

    xml_str = ElementTree.tostring(root, encoding='unicode', method='xml')

    server.create_job(args.job_name, xml_str)
