<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary bg-primary" data-bs-theme="dark">
        <div class="container-fluid">
        <a class="navbar-brand" href="#">Music Web</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">主页</a>
                </li>
                <li class="nav-item">
                <a class="nav-link" href="#">Features</a>
                </li>
                <li class="nav-item">
                <a class="nav-link" href="#">Pricing</a>
                </li>
                <li class="nav-item serach">
                    <input class="form-control me-2" type="search" placeholder="请输入想要查找的内容" aria-label="Search">
                </li>
                <li class="nav-item serach-btn">
                    <button class="btn btn btn-primary" type="submit">搜索</button>
                </li>
            </ul>
            <span class="navbar-text login">
                <button class="btn btn-outline-success me-2" type="button">登录</button>
            </span>
            <span class="navbar-text register">
                <button class="btn btn-outline-success me-2" type="button">注册</button>
            </span>
        </div>
        </div>
    </nav>
</template>

<script>
export default{

}
</script>


<style scoped>
.serach{
    margin-left: 40px;
    

}
.serach-btn{
    margin-left: 20px;
    transition: transform 0.5s cubic-bezier(0.68, -0.55, 0.27, 1.55); /* 调整过渡时间和缓动函数 */
    transition-delay: 0.2s;
}
.serach-btn:hover{
    cursor: pointer;
    color: black;
    transform: scale(1.3); /* 按钮放大到原始尺寸的1.1倍 */
    
}
</style>