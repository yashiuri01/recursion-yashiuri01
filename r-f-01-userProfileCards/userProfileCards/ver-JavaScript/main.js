document.addEventListener('DOMContentLoaded', () => {

  class Employee{
    constructor (firstName, lastName, job, skill, country, avatarUrl) {
      this.firstName = firstName;
      this.lastName = lastName;
      this.job = job;
      this.skill = skill;
      this.country = country;
      this.avatarUrl = avatarUrl;
    }

    getFullName(){
      return this.firstName + " " + this.lastName;
    }
  }

  function createEmployeeCard(employeeObject){
    // カード全体の定義
    let innerFlex = document.createElement("div");
    innerFlex.classList.add("d-flex", "align-items-center", "justify-content-start", "col-md-7", "col-10", "m-1");

    let cardDiv = document.createElement("div");
    cardDiv.classList.add("d-flex", "col-12", "profile-card");

    innerFlex.append(cardDiv);


    // カード左半分の定義
    let leftInfo = document.createElement("div");
    leftInfo.classList.add("col-8", "py-3");

    let div1 = document.createElement("div");
    div1.classList.add("py-2");
    let div2 = div1.cloneNode(true);
    let div3 = div1.cloneNode(true);

    // employeeName
    let nameTitle = document.createElement("h4");
    nameTitle.innerHTML = employeeObject.getFullName();

    // job
    let employeeJob = document.createElement("p");
    employeeJob.innerHTML = "Job: " + "<br>"  + employeeObject.job;
    div1.append(employeeJob);

    // skill
    let employeeSkill = document.createElement("p");
    employeeSkill.innerHTML = "Skill : <br>" + employeeObject.skill;
    div2.append(employeeSkill);

    // country
    let employeeCountry = document.createElement("p");
    employeeCountry.innerHTML = "Country :<br>" + employeeObject.country;
    div3.append(employeeCountry);

    // 要素の追加
    leftInfo.append(nameTitle);
    leftInfo.append(div1);
    leftInfo.append(div2);
    leftInfo.append(div3);


    // カード右半分の定義
    let rightInfo = document.createElement("div");
    rightInfo.classList.add("col-4", "d-flex", "justify-content-center", "align-items-center");

    let div4 = document.createElement("div");

    let avatar = document.createElement("img");
    avatar.classList.add("avatar");
    avatar.src = employeeObject.avatarUrl;

    div4.append(avatar);
    rightInfo.append(div4);

    //表示処理
    cardDiv.append(leftInfo);
    cardDiv.append(rightInfo);

    return innerFlex;
  }

  let profilesContainer = document.getElementById("profiles");

  let employee1 = new Employee("Kaiden", "Herman", "Software Engineer", "C++, C#, Java, PHP, JavaScript, Python","United States", "https://pbs.twimg.com/profile_images/501759258665299968/3799Ffxy.jpeg");
  let employee2 = new Employee("Elizabeth", "Dunn", "Accountant", "Excel, Word, Quickbooks", "England", "https://randomuser.me/api/portraits/women/76.jpg");
  let employee3 = new Employee("Duan", "Moreno", "Teacher",  "Working with children, History, Word", "Argentina", "https://randomuser.me/api/portraits/med/men/93.jpg");
  let employees = [employee1, employee2, employee3];

  if (profilesContainer) {
    employees.map(employee => profilesContainer.append(createEmployeeCard(employee)));
  } else {
    console.error('The container element with id "profiles" does not exist.');
  }
});
