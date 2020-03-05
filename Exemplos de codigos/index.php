<style>
    div{
        margin:5px
    }
    input{
        height:50px
    }
    button{
        height:40px
    }

</style>
<section>
    <form method='POST' action='exemplosCodigos.php'>
        <div>
            <input type="number" id="valor" placeholder="Digite um valor">
        </div>
        <div>
            <button id="cad">Ok</button> 
            <button id="parar">Parar</button>
        </div>
    <form>
</section>

<script>

    let btnOk =  document.getElementById('cad');
    let btnParar =  document.getElementById('parar');
    let values = [];

    btnOk.addEventListener('click', function(){
        let input =  document.getElementById('valor');
        values[]= input.value;
    });


    btnParar.addEventListener('click',function(){

    });

    function prepararUrl(values){
        return 
    }
</script>
