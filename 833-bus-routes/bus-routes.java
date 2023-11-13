class Solution{

public static int numBusesToDestination(
	final int[][] routeToStops,
	final int src,
	final int dst
){
	Map<Integer, List<Integer>> stopToRoutes = new HashMap<>();
	for (int route = 0; route < routeToStops.length; route += 1){
		for (final int stop : routeToStops[route]){
			List<Integer> routes = stopToRoutes.getOrDefault( stop, new ArrayList<>() );
			routes.add(route);
			stopToRoutes.put(stop, routes);
		}
	}

	Set<Integer> visitedRoutes = new HashSet<>();
	Set<Integer> visitedStops = new HashSet<>();
	Queue<Integer> bfsQueue = new LinkedList<>();

	if (src == dst){
		return 0;
	}
	visitedStops.add(src);
	bfsQueue.add(src);

	for (int busCnt = 1; !bfsQueue.isEmpty(); busCnt += 1){
		for (int cntDown = bfsQueue.size(); cntDown > 0; cntDown -= 1){
			final int curStop = bfsQueue.remove();

			for ( final int nextRoute : stopToRoutes.get(curStop) ){
				if ( visitedRoutes.contains(nextRoute) ){
					continue;
				}

				visitedRoutes.add(nextRoute);
				for (final int nextStop : routeToStops[nextRoute]){
					if ( visitedStops.contains(nextStop) ){
						continue;
					}

					if (nextStop == dst){
						return busCnt;
					}
					visitedStops.add(nextStop);
					bfsQueue.add(nextStop);
				}
			}
		}
	}

	return -1;
}

}