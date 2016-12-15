chrome.contextMenus.create({
	title: 'Validate: %s',
	contexts: ['page'],
	onclick: Validate
});

function searchText(info){
	var myQuery = encodeURI('https://www.google.com/search?q=' + info.selectionText);
	chrome.tabs.create({
		url: myQuery
	});
}