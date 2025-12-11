<h1 id="lexema-ecm" style="text-align: center; margin-bottom: 30px; color: #000000ff;">
  <a style="color: inherit; text-decoration: none;">Руководство администратора Lexema-EPR</a>
</h1>

<div class="menu">
  <!-- Группа 1: Настройка системы -->
  <div class="group">
    <h2 class="group-title">Настройка системы</h2>
    <div class="group-content">
      <div class="button-row">
        <a href="Admin manuals\Настройка документов\" class="button">Настройка документов</a>
        <a href="Admin manuals\Конструктор документов\" class="button">Настройка конструктора документов</a>
        <a href="Admin manuals\Конструктор документов\#вычисляемые_атрибуты" class="button">Вычисляемые атрибуты в конструкторе</a>
        <a href="Admin manuals\Подтипы документов\" class="button">Настройка подтипов</a>
      </div>
      <div class="button-row">
        <a href="Admin manuals\Настройка шаблонов маршрутов\" class="button">Настройка шаблонов маршрутов</a>
        <a href="Admin manuals\Настройка шаблонов маршрутов\#сервисные_функции" class="button">Служебные пользователи в маршруте</a>
        <a href="Admin manuals\Настройка служебных пользователей\" class="button">Вычисляемый пользователь в маршруте</a>
      </div>
      <div class="button-row">
        <a href="Admin manuals\Планировщик задач\" class="button">Создание задачи в планировщике</a>
        <a href="Admin manuals\Функции планировщика задач\" class="button">Функции планировщика задач</a>
      </div>
      <div class="button-row">
        <a href="Admin manuals\Настройка правил поиска для ЖСД\" class="button">Настройка правил поиска для ЖСД</a>
      </div>
    </div>
  </div>
  
  <!-- Группа 2: Работа с пользователями -->
  <div class="group">
    <h2 class="group-title">Работа с пользователями</h2>
    <div class="group-content">
      <div class="button-row">
        <a href="Admin manuals\Управление пользователями\" class="button">Создание пользователя в системе</a>
        <a href="Admin manuals\Автоматическое создание пользователей\" class="button">Автоматическое создание пользователей</a>
      </div>
      <div class="button-row">
        <a href="Admin manuals\Бизнес-роли\" class="button">Бизнес-роли</a>
        <a href="Admin manuals\Технические роли\" class="button">Роли на документы</a>
        <a href="Admin manuals\Настройка пользователей\#документооборот" class="button">Настройка горизонтальных прав</a>
        <a href="Admin manuals\Управление пользователями\#замещаемые" class="button">Настройка замещения</a>
      </div>
      <div class="button-row">
        <a href="Admin manuals\Выпуск ОНЭП\" class="button">Выпуск электронной подписи</a>
        <a href="Admin manuals\Настройка для токенов КЭП\" class="button">Привязка УКЭП к пользователю</a>
      </div>
    </div>
  </div>
  
  <!-- Группа 3: Справочные материалы -->
  <div class="group">
    <h2 class="group-title">Справочные материалы</h2>
    <div class="group-content">
      <div class="button-row">
        <a href="Admin manuals\FAQ\" class="button">FAQ</a>
        <a href="Admin manuals\Настройка констант\" class="button">Настройка констант</a>
      </div>
    </div>
  </div>
</div>

<style>
.menu {
  display: flex;
  flex-direction: column;
  gap: 30px;
  width: 100%;
  max-width: 1600px;
  margin: 0 auto;
  padding: 0 20px;
}

.group {
  margin-bottom: 30px;
}

.group-title {
  color: #1a252f;
  font-size: 1.5em;
  margin: 0 0 15px 0;
  padding-bottom: 8px;
  border-bottom: 2px solid #68bb6c;
  text-align: center;
}

.group-content {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.button-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center; /* Центрируем кнопки */
  width: 100%;
}

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 15px 30px;
  background: #68bb6c;
  color: white !important;
  text-decoration: none;
  border-radius: 5px;
  font-size: 1.1em;
  box-sizing: border-box;
  transition: all 0.3s ease;
  border: 2px solid transparent;
  white-space: nowrap;
  min-width: 200px;
  text-align: center;
}

.button:hover {
  background: #fa7c06ff;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  border-color: #1a252f;
  outline: none;
}

@media (max-width: 768px) {
  .button {
    min-width: 150px;
    padding: 12px 20px;
    font-size: 1em;
  }
  
  .group-title {
    font-size: 1.3em;
  }
}

@media (min-width: 768px) {
  h1 {
    font-size: 2.5em;
  }
  
  h1 a:hover {
    text-decoration: underline;
  }
  
  .group-title {
    font-size: 1.8em;
  }
}

/* Остальные стили остаются без изменений */
.md-grid {
  max-width: 98%;
}

ol.oldec, ol.oldec li, ol.oldec li:before {
  list-style-type: decimal;
}

ul.uldisc {
  list-style-type: disc;
}

ul.ulcircle {
  list-style-type: circle;
}

img {
  border: 1px solid #9f9f9f;
  transition: transform ease-in-out 0.5s;
}

img:active[src*="#zoom"] {    
  cursor: zoom-out;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  margin-top: 75px;
  margin-bottom: auto;
  margin-left: auto;
  margin-right: auto;
  width: 1200px;
  height: auto;
}

img[src*="#zoom"] {
  cursor: zoom-in;
}

.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.zoom {
  transition: transform ease-in-out 0.5s;
  cursor: zoom-in;
}

.image-zoom-large {
  cursor: zoom-out;
  z-index: 100;
  position: absolute;
  left: 50%;
  transform: translate(-50%, 0%);
  text-align: center;
  margin-top: 0px;
  margin-bottom: auto;
  margin-left: auto;
  margin-right: auto;
  width: 1100px;
  height: auto;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

table {
  word-break: break-word;
}

tbody tr:nth-child(odd) {
  background-color: #f3f3f3;
}
</style>
<!-- 
# Руководство администратора системы

## Введение

**Lexema-ECM** — комплексная система управления корпоративным контентом, включающая в себя автоматизацию работы с кадровыми документами.

Руководство предназначено:

- для специалистов, которым необходимо обрабатывать электронные документы в Lexema-ECM: создавать карточки, отправлять по маршруту согласования и подписывать документы электронной подписью;

- для специалистов, которым необходимо администрировать проект: создавать новые типы карточек, настраивать маршруты и наполнять справочники системы данными;
 
## Назначение Lexema-ECM

**Lexema-ECM**  имеет богатый функционал типовой конфигурации — от канцелярии до юридически значимого кадрового документооборота, а также широкие возможности для развития системы и подключения дополнительных функций. 
В системе настроены типовые карточки по работе с договорами, письмами, поручениями, служебными записками, приказами, заявления от сотрудников и ЛНА по кадровому документообороту, а также преднастроены маршруты по их обработке. Документы готовы к использованию сразу после развертывания системы. Поэтому можно в кратчайший срок начать получать бонусы от электронного согласования документов. 

В **Lexema-ECM** встроен сервис, позволяющий одним нажатием кнопки выпускать облачные неквалифицированные электронные подписи для сотрудников компании. Использование таких подписей гарантирует легитимность документов КЭДО и позволяет подписывать электронные документы с любого устройства без привязки к рабочему месту. Выпуск УНЭП с помощью Lexema-ECM не требует дополнительной покупки.

## Настройка и развитие Lexema-ECM

**Lexema-ECM** можно развивать своими силами. Для этого есть следующие инструменты: 

* Конструктор для настройки документов. С его помощью даже без знаний в программировании можно настроить новые или внести изменения в старые карточки, править печатные формы и маршруты согласования.

* Более сложные задачи развития Lexema-ECM решаются в **Lexema-Framework**. Это современная платформа для быстрой разработки веб-приложений, среда разработки Lexema-ECM. В платформе используется стек современных популярных программных технологий, которыми в настоящее время владеют очень многие программисты. ИТ-специалисты любой компании могут пройти бесплатное онлайн-обучение в Академии Lexema по программированию на **Lexema-Framework** и в последствии самостоятельно развивать Lexema-ECM, решая даже самые сложные задачи.

## Области применения

Кроме документов типовой конфигурации, к электронному документообороту в Lexema-ECM можно подключать любые новые документы, требующие электронного согласования или подписания. Это могут быть производственные документы, документы складского учета, финансового учета. 

Также Lexema-ECM имеет дополнительные модули, которыми можно расширить систему: робот по распознаванию и обработке первичных входящих документов и платформу для дистанционного корпоративного обучения.  -->