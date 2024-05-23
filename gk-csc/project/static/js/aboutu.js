const a1=`<button onclick="backward(1)"><img src="../static/src/back.jpg" alt="" id="bacw"></button>
        <div class="about">
    <p>
    В самом начале своего пути "Кавказ Строй Континент" была маленькой семейной компанией в Ставрополе, основанной братьями Аланом и Давидом Хасановыми. Они унаследовали любовь к строительству от своего отца, который был опытным мастером-строителем.</p>
    <img src="../static/src/история-1.jpg">
</div><button onclick="forward(1)" ><img src="../static/src/forw.jpg" alt="" id="forw"></button>`
const a2=`<button onclick="backward(2)"><img src="../static/src/back.jpg" alt="" id="bacw"></button><div class="about">
    <p>
        С первых дней своей работы братья поставили перед собой цель создать компанию, которая не только будет строить качественные дома, но и будет служить примером профессионализма и надежности. Они верили, что каждый дом, построенный их компанией, должен быть не просто строением, а уютным домом, в котором счастливо проживают его обитатели.
    </p>
    <img src="../static/src/история-2.jpg">
</div><button onclick="forward(2)" ><img src="../static/src/forw.jpg" alt="" id="forw"></button>`
const a3=`<button onclick="backward(3)"><img src="../static/src/back.jpg" alt="" id="bacw"></button><div class="about">
    <p>
        С течением времени "Кавказ Строй Континент" стала известной и уважаемой компанией в Ставрополе. Ее проекты отличались высоким качеством строительства, современным дизайном и инновационными технологиями. Братья Хасановы постоянно внедряли новые методы и материалы, чтобы улучшить свои проекты и удовлетворить потребности своих клиентов.
    </p>
    <img src="../static/src/история-3.png">
</div><button onclick="forward(3)" ><img src="../static/src/forw.jpg" alt="" id="forw"></button>`
const a4=`<button onclick="backward(4)"><img src="../static/src/back.jpg" alt="" id="bacw"></button><div class="about">
    <p>
        Однако путь к успеху не был легким. В начале своего пути компания столкнулась с различными трудностями и препятствиями, такими как финансовые затруднения и конкуренция на рынке. Но благодаря упорному труду, профессионализму и преданности своей мечте, братья смогли преодолеть все трудности и построить успешный бизнес.
    </p>
    
</div><button onclick="forward(4)" ><img src="../static/src/forw.jpg" alt="" id="forw"></button>`
const a5=`<button onclick="backward(5)"><img src="../static/src/back.jpg" alt="" id="bacw"></button><div class="about">
    <p>
    Сегодня "Кавказ Строй Континент" остается лидером на рынке строительства в Ставрополе. Их проекты украшают город и приносят радость и комфорт его жителям. Братья Хасановы продолжают развивать свою компанию, стремясь к новым высотам и сохраняя свою приверженность качеству и надежности.
    <img src="../static/src/история-5.jpg">
</div><button onclick="forward(5)" ><img src="../static/src/forw.jpg" alt="" id="forw"></button>`

function forward(num){
	let elem=document.getElementById('about-wrapper')
	switch (num)
    {
        case 1: 
        elem.innerHTML=a2
        break
        case 2: 
        elem.innerHTML=a3
        break
        case 3: 
        elem.innerHTML=a4
        break
        case 4: 
        elem.innerHTML=a5
        break
        case 5: 
        elem.innerHTML=a1
        break
    }
}
function backward(num){
    let elem=document.getElementById('about-wrapper')
    switch (num)
    {
        case 1: 
        elem.innerHTML=a5
        break
        case 2: 
        elem.innerHTML=a1
        break
        case 3: 
        elem.innerHTML=a2
        break
        case 4: 
        elem.innerHTML=a3
        break
        case 5: 
        elem.innerHTML=a4
        break
    }
}