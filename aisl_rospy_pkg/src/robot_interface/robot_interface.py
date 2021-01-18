#! /usr/bin/env python

import rospy

class RobotInterface(object):
    def __init__(self):
        # rospy.loginfo('[RobotInterface] Constructor called')
        print('[RobotInterface] Constructor called')

        self.name = 'Robot'

    def pass_object(self):
        # rospy.logwarn('[RobotInterface] pass_object() not implemented yet')
        print('[RobotInterface] pass_object() not implemented yet')

    def speak(self):
        # rospy.logwarn('[RobotInterface] speak() not implemented yet')
        print('[RobotInterface] speak() not implemented yet')

    def fetch_object(self):
        # rospy.logwarn('[RobotInterface] fetch_object() not implemented yet')
        print('[RobotInterface] fetch_object() not implemented yet')

    def put_object(self):
        # rospy.logwarn('[RobotInterface] put_object() not implemented yet')
        print('[RobotInterface] put_object() not implemented yet')

    def move_to_neutral(self):
        # rospy.logwarn('[RobotInterface] put_object() not implemented yet')
        print('[RobotInterface] move_to_neutral() not implemented yet')
