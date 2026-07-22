# import React from 'react';
# // function App() {
# //   return (
# //     <div>
# //       <h1>Hello Yash!</h1>
# //       <p>This is my first react component</p>
# //     </div>
# //   );
# // }
# // export default App;

# // function App() {
# //   const name = 'Yash';
# //   const internshipdays = 60;
# //   const isActive = true;
# //   const testsPassing = 100

# //   return (
# //     <div>
# //       <h1> Hello, {name}!</h1>
# //       <p> your internship duration is {internshipdays}</p>
# //       <p> status : {isActive ? 'Active' : 'Inactive'}</p>
# //       <p> double the days {internshipdays * 2}</p>
# //       <p> the project test cases passed are {testsPassing}</p>
# //     </div>
# //   );
# // }
# // export default App;

# // function ModuleCard(props) {
# //   return (
# //     <div>
# //       <h2>{props.moduleName}</h2>
# //       <p>Health Score : {props.healthScore}</p>
# //       <p>Owner : {props.owner}</p>
# //     </div>
# //   );
# // }

# // function App() {
# //   return (
# //     <div>
# //       <h1>OIS DASHBOARD</h1>
# //       <ModuleCard moduleName="auth_service.py" healthScore={92} owner="Yash" />
# //       <ModuleCard moduleName="db_utils.py" healthScore={80} owner="Priya" />
# //       <ModuleCard
# //         moduleName="legacy_parser.py"
# //         healthScore={30}
# //         owner="Rahul"
# //       />
# //     </div>
# //   );
# // }

# // export default App;

# // function ModuleCard({ moduleName, healthScore, owner, dependancyCount }) {
# //   return (
# //     <div>
# //       <h2> {moduleName} </h2>
# //       <p> health score : {healthScore} </p>
# //       <p> owner : {owner} </p>
# //       <p> dependancy count : {dependancyCount} </p>
# //     </div>
# //   );
# // }

# // function App() {
# //   return (
# //     <div>
# //       <h1> OIS DASHBOARD </h1>
# //       <ModuleCard
# //         moduleName="auth_service.py"
# //         healthScore={92}
# //         owner="Yash"
# //         dependancyCount={4}
# //       />
# //       <ModuleCard
# //         moduleName="db_utils.py"
# //         healthScore={80}
# //         owner="Priya"
# //         dependancyCount={7}
# //       />
# //     </div>
# //   );
# // }
# // export default App;

# function ModuleCard({ moduleName, healthScore, owner, dependancyCount }) {
#   return (
#     <div>
#       <h2> {moduleName} </h2>
#       <p> health score : {healthScore} </p>
#       <p> owner : {owner} </p>
#       <p> dependancy count : {dependancyCount} </p>
#     </div>
#   );
# }

# function App() {
#   const modules = [
#     {
#       moduleName: 'auth_service.py',
#       healthScore: 92,
#       owner: 'Yash',
#       dependancyCount: 4,
#     },
#     {
#       moduleName: 'utils_db.py',
#       healthScore: 80,
#       owner: 'Priya',
#       dependancyCount: 7,
#     },
#     {
#       moduleName: 'legacy_parser.py',
#       healthScore: 92,
#       owner: 'Rahul',
#       dependancyCount: 3,
#     },
#   ];
#   return (
#     <div>
#       <h1> OIS DASHBOARD </h1>
#       {modules.map((mod) => (
#         <ModuleCard
#           key={mod.moduleName}
#           moduleName={mod.moduleName}
#           healthScore={mod.healthScore}
#           owner={mod.owner}
#           dependancyCount={mod.dependancyCount}
#         />
#       ))}
#     </div>
#   );
# }

# export default App;
