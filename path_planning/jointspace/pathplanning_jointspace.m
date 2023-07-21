%%           Path Planning, Trajectory Generation and Inverse Kinematics Solving 
clear
clc

%%              Loading and Showing the Robot
load 'robot.mat'
endeffector = 'Link_6';
robot.DataFormat = 'row';
conf=robot.homeConfiguration;
axes=show(robot,conf,'Frames','off','PreservePlot',false);
xlim([-1 1]), ylim([-1 1]), zlim([0 1.2])
axis auto;
view([45 30]);

%%          creating and plotting way points
waypointType = 'final';
switch waypointType
    case 'p2p'
        waypoints = [0.45 -0.3 0.44; 0.45 -0.6 0.44]';
        waypointTimes = [0 6];
    case 'circle'
        radius = 0.6;
        t= (0:2:12)';
        theta= t*(2*pi/t(end))-(pi/2);
        points = [0 0 0.5] + radius * [cos(theta) sin(theta) 0*ones(size(theta))];
        waypoints = points';
        waypointTimes=0:2:12;
    case 'final'
        points=[0.425 0.0161 -0.0867;
        0.425 0.0161 -0.3031;
        0.425 0.0161 -0.0867;
        -0.2895    0.4691   -0.0867
        -0.425 -0.0161 -0.0867;
        -0.425 -0.0161 -0.3031;
        -0.425 -0.0161 -0.0867;
        -0.2895    0.4691   -0.0867;
        0.425 0.0161 -0.0867];
        waypoints=points' ;
        waypointTimes =0:2:16;
end

ts=0.2;
trajtimes=0:ts:waypointTimes(end);        
hold on 
plot3(waypoints(1,:),waypoints(2,:),waypoints(3,:),'go','LineWidth',2);
axis auto;
view([45 30]);
