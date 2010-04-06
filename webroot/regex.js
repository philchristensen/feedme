var LIMIT = 10;

function displayRegexResults(result){
	$('#form-item-regex_check textarea').val(result['source']);
	
	var display = $('#result-breakdown');
	display.empty();
	
	var total = result.matches.length;
	
	display.append($('<h3>Found ' + total + ' Items</h3>'));
	if(total > LIMIT){
		display.append($('<h4>(only showing first 10 results)</h4>'));
	}
	for(var index in result.matches){
		var match = result.matches[index];
		
		var groups = $('<div class="groups"></div>');
		for(var group_index in match.groups){
			var group = match.groups[group_index];
			if(group_index == 0){
				groups.append($('<div class="first group">' + group + '</div>'));
			}
			else{
				groups.append($('<div class="group">' + group + '</div>'));
			}
		}
		
		var named_groups = $('<div class="named-groups"></div>');
		for(var key in match.named_groups){
			var group = match.named_groups[key];
			named_groups.append($('<div class="group"><span class="key">' + key + '</span> => <span class="value">' + group + '</span></div>'));
		}
		
		
		var matchElement = $('<div class="match"></div>');
		matchElement.append($('<strong>Groups:</strong>'));
		matchElement.append(groups);
		matchElement.append($('<strong>Named Groups:</strong>'));
		matchElement.append(named_groups);
		display.append(matchElement);
		
		if(parseInt(index) + 1 == LIMIT){
			break;
		}
	}
}

function testRegex(url, pattern){
	$.ajax({
		type	: "POST",
		url		: '/feeds/test',
		data	: {
			'url'		: url,
			'pattern'	: pattern,
		},
		dataType: "json",
		success	: displayRegexResults,
	});
}