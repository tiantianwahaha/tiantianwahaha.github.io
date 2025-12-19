window.onload = function() {
    // ==============================================
    // 1. 地图初始化
    // ==============================================
    // 修正：恢复原来的坐标 [-243.60874]，确保能看到标记点
    var mymap = L.map('mapid').setView([39.90733, -243.60874], 5);

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
            '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
        id: 'mapbox.streets'
    }).addTo(mymap);

    // ==============================================
    // 2. 足迹数据配置 (在这里修改颜色和内容)
    // ==============================================
    // 格式说明：
    // lat: 纬度, lng: 经度, 
    // title: 标题, img: 图片路径 (没有图片填 null), 
    // color: 图标颜色 ('red', 'orange', 'blue', 'green', 'purple', 'darkred', 'cadetblue')
    const locations = [
        {
            lat: 39.90904, 
            lng: -243.7282, 
            title: "2022.8 七夕", 
            img: "image/eshi.jpg",
            color: "orange"
        },
        {
            lat: 40.25596, 
            lng: -243.71349, 
            title: "2022.9 蟒山森林公园", 
            img: "image/mangshan.jpg",
            color: "red"
        },
        {
            lat: 43.2777, 
            lng: -275.71965, 
            title: "2024.09 新疆独库", 
            img: "image/duku.jpg",
            color: "green"
        },
        {
            lat: 45.75024, 
            lng: -233.36526, 
            title: "2024.12 哈尔滨", 
            img: "image/duku.jpg",
            color: "blue"
        },		
		{
            lat: 29.35404, 
            lng: -249.51029, 
            title: "2025.5 张家界", 
            img: null, // 没有图片
            color: "orange"
        },
		{
            lat: 36.05241, 
            lng: -248.51262, 
            title: "2025.10 山西临汾", 
            img: null, // 没有图片
            color: "orange"
        },
		{
            lat: 29.54469, 
            lng: -253.45293, 
            title: "2025.11 重庆", 
            img: null, // 没有图片
            color: "orange"
        },
		{
            lat: 18.32302, 
            lng: -250.44102, 
            title: "2025.11 海南三亚", 
            img: null, // 没有图片
            color: "blue"
        },
    ];

    // ==============================================
    // 3. 自动生成图标 (无需修改)
    // ==============================================
    locations.forEach(function(loc) {
        // 创建图标
        var icon = L.AwesomeMarkers.icon({
            icon: 'heart', 
            prefix: 'fa', 
            markerColor: loc.color || 'orange', // 默认颜色
            iconColor: '#ffffff'
        });

        // 准备弹窗内容
        var popupContent = "<b>" + loc.title + "</b>";
        if (loc.img) {
            popupContent += "<br /><img src='" + loc.img + "' width='100%' />";
        }

        // 添加到地图
        L.marker([loc.lat, loc.lng], {icon: icon})
            .addTo(mymap)
            .bindPopup(popupContent);
    });

    // ==============================================
    // 4. 辅助功能
    // ==============================================
    var popup = L.popup();
    function onMapClick(e) {
        popup
            .setLatLng(e.latlng)
            .setContent("当前坐标: " + e.latlng.toString())
            .openOn(mymap);
        console.log("坐标:", e.latlng);
    }
    mymap.on('click', onMapClick);
};