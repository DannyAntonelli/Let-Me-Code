import { getProject } from "@/api/project.js";
export function retrieveProjectInfo(id, context) {
  getProject(id)
    .then((response) => {
      console.log(response);
      context.file_ids = response.file_ids;
      context.description = response.description;
      context.id = response.id;
      context.is_public = response.is_public;
      context.name = response.name;
      context.shared_users = response.shared_users;
      context.user = response.user;
      context.getFiles();
    })
    .catch((error) => {
      console.log(error);
    });
}
export function buildTree(files) {
  let tree = {};
  for (let file of files) {
    let path = file.name.split("/");
    let curr = tree;
    for (let i = 0; i < path.length; i++) {
      if (i == path.length - 1) {
        file.fileName = path[i];
        curr[path[i]] = file;
      } else {
        if (curr[path[i]] == undefined) {
          curr[path[i]] = {
            folderName: path.slice(0, i + 1).join("/") + "/",
          };
        }
        curr = curr[path[i]];
      }
    }
  }
  tree["root"] = tree[""];
  delete tree[""];
  if (tree["root"] == undefined) {
    tree["root"] = {
      folderName: "/",
    };
  }
  console.log(tree);
  return tree;
}
