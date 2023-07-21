%ip_ad = "192.168.56.101";
%rosinit('192.168.56.101', 11311)
rosinit('http://192.168.56.105:11311');
%rosinit('http://localhost:11311')

    
% specify topics that message is going to be published
pub1 = rospublisher('/ur5/joint1_position_controller/command', 'std_msgs/Float64');
pub2 = rospublisher('/ur5/joint2_position_controller/command', 'std_msgs/Float64');
pub3 = rospublisher('/ur5/joint3_position_controller/command', 'std_msgs/Float64');
pub4 = rospublisher('/ur5/joint4_position_controller/command', 'std_msgs/Float64');
pub5 = rospublisher('/ur5/joint5_position_controller/command', 'std_msgs/Float64');
pub6 = rospublisher('/ur5/joint6_position_controller/command', 'std_msgs/Float64');


% values to be published to the above topics from generated trajectory
td1 = q(1,:);
td2 = q(2,:);
td3 = q(3,:);
td4 = q(4,:);
td5 = q(5,:);
td6 = q(6,:);


% Create a message to send
% publish the message to the topics specified
msg1 = rosmessage(pub1);
msg2 = rosmessage(pub2);
msg3 = rosmessage(pub3);
msg4 = rosmessage(pub4);
msg5 = rosmessage(pub5);
msg6 = rosmessage(pub6);


while 1
    for i=1:81
        msg1.Data = td1(i)
        msg2.Data = td2(i)
        msg3.Data = td3(i)
        msg4.Data = td4(i)
        msg5.Data = td5(i)
        msg6.Data = td6(i)
        
        % wait for 0.5sec for the next move.
        pause(0.5)

        % Send the message via the publisher.    
        send(pub1, msg1)
        send(pub2, msg2)
        send(pub3, msg3)
        send(pub4, msg4)
        send(pub5, msg5)
        send(pub6, msg6)
    end   
end


