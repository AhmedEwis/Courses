olditer = maxiter;
maxi = get(gcbo,'String');
maxiter = str2num(maxi); 
if maxiter > 200 
  maxiter = olditer;
  men1= uicontrol('Parent',men, ...
	'Backgroundcolor',[1 1 1], ...
	'Foreground',[1 0 0], ...
	'Units','points', ...
	'Position',[10 40 250 20], ...	
	'Style','text', ...
 	'Fontsize',12, ...
	'string','No more than 200 iterations', ...
	'Tag','StaticText1');
else
  antaliter = maxi;
  men1= uicontrol('Parent',men, ...
	'Backgroundcolor',[1 1 1], ...
	'Foreground',[0 0 0], ...
	'Units','points', ...
	'Position',[155 166 140 20], ...	
	'Style','text', ...
 	'Fontsize',12, ...
	'string',antaliter, ...
	'Tag','StaticText1');
  whitecomnotmy
end
if yyy == 1
  whitelosilp
  setoffilp;
  rita
  setonilp;
end
yyy = 0;