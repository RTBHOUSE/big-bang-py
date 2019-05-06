import invoke

from . import dependencies as dependencies_tasks
from . import project as project_tasks
from . import release as release_tasks

# The main namespace MUST be named `namespace` or `ns`.
# See: http://docs.pyinvoke.org/en/1.2/concepts/namespaces.html
namespace = invoke.Collection()

namespace.add_task(project_tasks.coverage_report)
namespace.add_task(project_tasks.flake8_report)
namespace.add_task(project_tasks.linters)
namespace.add_task(release_tasks.make_release)
namespace.add_task(project_tasks.set_precommit)
namespace.add_task(project_tasks.run_tests)

dependencies_namespace = invoke.Collection("dependencies")
dependencies_namespace.add_task(dependencies_tasks.compile)
dependencies_namespace.add_task(dependencies_tasks.sync_dev)
namespace.add_collection(dependencies_namespace)
