using UnityEngine;

public class PortalDirection : MonoBehaviour
{
    Collider2D mainCollider;

    [SerializeField] [Range(-1,1)] public int horizontalDirection;
    [SerializeField] [Range(-1, 1)] public int verticalDirection;

    [HideInInspector] public Vector3 groundCheckPos;

    // Start is called before the first frame update
    void Awake()
    {
        mainCollider = GetComponent<Collider2D>();
    }

    void FixedUpdate()
    {
        Bounds colliderBounds = mainCollider.bounds;
        groundCheckPos = colliderBounds.min + new Vector3(colliderBounds.size.x * 0.5f, colliderBounds.size.y * 0.5f, 0);
        // Check if player is grounded

        // Simple debug
        Debug.DrawLine(groundCheckPos, groundCheckPos - new Vector3(0.53f * horizontalDirection, 0.53f * verticalDirection, 0), Color.green);

        
    }
}
