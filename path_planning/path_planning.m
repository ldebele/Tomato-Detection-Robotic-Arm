ur5 = loadrobot("universalUR5");
ur5.DataFormat = 'column';
q_home = [0 0 0 0 0 0]'*pi/180;
eeName = 'wrist_1_link';
% showdetails(ur5)
%path
points=[0.425 0.0161 -0.0867;
       0.425 0.0161 -0.3031;
       0.425 0.0161 -0.0867;
       -0.2895    0.4691   -0.0867
       -0.425 -0.0161 -0.0867;
       -0.425 -0.0161 -0.3031;
       -0.425 -0.0161 -0.0867;
        -0.2895    0.4691   -0.0867;
        0.425 0.0161 -0.0867];
waypoints=points'
waypointTimes =0:2:16;
ts =0.2;  
trajTimes = 0:ts:waypointTimes(end);

numWaypoints = size(waypoints,2);
numJoints = numel(ur5.homeConfiguration);

%%Create Inverse Kinematics Solver and Set Parameters
ik = inverseKinematics('RigidBodyTree',ur5);
ikWeights = [0 0 0 1 1 1];
ikInitGuess = q_home';
ikInitGuess(ikInitGuess > pi) = ikInitGuess(ikInitGuess > pi) - 2*pi;
ikInitGuess(ikInitGuess < -pi) = ikInitGuess(ikInitGuess < -pi) + 2*pi;

%%Set Plot and Display Waypoints
show(ur5,q_home,'Frames','on','PreservePlot',false);
axis auto;
view([30 15]);
hold on
hTraj = plot3(waypoints(1,1),waypoints(2,1),waypoints(3,1),'g-');
plot3(waypoints(1,:),waypoints(2,:),waypoints(3,:),'go','LineWidth',2);
axis auto;
view([30 15]);

%%Solve the Inverse Kinematics for Each Waypoint


jointWaypoints = zeros(numJoints,numWaypoints);

tgtPose = trvec2tform(waypoints(:,1)');
[config,info] = ik(eeName,tgtPose,ikWeights',ikInitGuess');

    jointWaypoints(:,1) = config';
for i = 2:numWaypoints
     tgtPose = trvec2tform(waypoints(:,i)');
     [config,info] = ik(eeName,tgtPose,ikWeights',jointWaypoints(:,i-1));
    
       jointWaypoints(:,i) = config';
              
end



%%Generate a Trajectory in Joint Space using Interpolation
    
  [q,qd,qdd] = cubicpolytraj(jointWaypoints,waypointTimes,trajTimes);

% Save the trajectory data 
Trajdata = zeros(3,numel(trajTimes));
TrajData = q;
Td1= TrajData(1,:);
Td2 = TrajData(2,:);
Td3 = TrajData(3,:);
%%Visualize the Solution
chk = zeros(5,3);
counter=0;
while(1)    
for i = 1:numel(trajTimes)

 
    config = q(:,i)';
    %config = k(:,i)';
    
    %config = config + q_homes';

    % Find Cartesian points for visualization
    eeTform = getTransform(ur5,config',eeName);
    eePos = tform2trvec(eeTform);
    set(hTraj,'xdata',[hTraj.XData eePos(1)], ...
              'ydata',[hTraj.YData eePos(2)], ...
              'zdata',[hTraj.ZData eePos(3)]);
    chk(i,:)=eePos;
    
  %Show the robot
  show(ur5,config','Frames','on','PreservePlot',false);
  num2str(trajTimes(i) + (counter * 16))
  title(['Trajectory at t = ' num2str(trajTimes(i) + (counter * 16))])
  drawnow   
end
counter=counter+1;
end   